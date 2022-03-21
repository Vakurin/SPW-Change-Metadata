import json
from datetime import datetime
from urllib.request import Request, urlopen
from utility import read_json, read_updated_json, write_file, get_img_url
from pathlib import Path

# update every day
# 6, 13, 20, 27 add -dogs if necessary
DEAD_IMG_URL = get_img_url('29')


def find_alive_mint_ids(mint_ids: list):
    alive_ids: list = read_json('alive_mint_ids.json')
    immunity: list = read_updated_json("immunity.json")
    return list(filter(lambda mint: mint in alive_ids and mint not in immunity, mint_ids))
    # return mint_ids


def find_mint_ids_by_att(data: list, trait_type: str, trait_value: str):
    count = 0
    mint_ids = []
    # for every element in json file
    for el in data:
        mint = el['mint']
        # for attributes for search
        for att in el['metadata']['attributes']:
            if (att['trait_type'] == trait_type) and (att['value'] == trait_value):
                count += 1
                mint_ids.append(mint)
    print(f"Find total {count} mints with trait {trait_type}:{trait_value}")
    return mint_ids


def kill_mint_ids(data: list, mint_ids_to_kill: list, all_ids: list):
    folder = datetime.now().strftime("%d_%b(%H:%M)")
    Path("../change_meta/" + folder).mkdir(parents=True, exist_ok=True)
    dead_ids = read_json("dead_mint_ids.json")

    for el in data:
        mint = el['mint']
        if mint in mint_ids_to_kill:
            for att in el['metadata']['attributes']:
                if att["trait_type"] == "isAlive":
                    att['value'] = "False"
                el['metadata']['image'] = DEAD_IMG_URL
                write_file(data=el['metadata'], name='change_meta/' + folder + '/' + mint)
                if mint not in dead_ids:
                    dead_ids.append(mint)
    write_file(dead_ids, 'data/dead_mint_ids')
    subtract_deads_from_alive(all_ids)


def subtract_deads_from_alive(all_ids: list):
    dead_ids: list = read_json("dead_mint_ids.json")
    alive_ids = subtract_lists(dead_ids, all_ids)
    write_file(alive_ids, 'data/alive_mint_ids')


def get_mint_att_dict(data: list, trait_type):
    mint_att_dict = dict()
    for el in data:
        mint = el['mint']
        for att in el['metadata']['attributes']:
            if att['trait_type'] == trait_type:
                mint_att_dict[mint] = att
    return mint_att_dict


def get_holders_with_alive_mints(mints_number: int, holders: dict):
    holders_mints = dict()
    for value, key in holders.items():
        alive_mints = find_alive_mint_ids(key['mints'])
        if len(alive_mints) >= mints_number:
            holders_mints[value] = alive_mints
    # write_file(holders_mints, 'test')
    return holders_mints


def get_listed_mints_magiceden_metadata(collection: str):
    mints = []
    counter = 0
    while True:
        url = f'https://api-mainnet.magiceden.io/rpc/getListedNFTsByQuery?q={{"$match":' \
              f'{{"collectionSymbol":"{collection}"}},"$skip":{counter}}}'
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        results: list = json.loads(web_byte.decode('utf-8'))['results']
        counter += 20
        mints.extend(results)
        if len(results) == 0:
            break
    return mints


def get_mints_ids_from_magiceden_metadata(magiceden_metadata: list):
    result = []
    alive_ids: list = read_json('alive_mint_ids.json')
    prices = dict()
    for el in magiceden_metadata:
        mintAddress = el['mintAddress']
        result.append(mintAddress)
        if mintAddress in alive_ids:
            prices[mintAddress] = el['price']
    write_file(prices, "test")
    return result


def subtract_lists(to_subtract: list, from_subtract: list):
    return list(set(from_subtract) - set(to_subtract))
