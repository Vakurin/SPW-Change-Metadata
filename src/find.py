from utility import read_json
from utility import write_file

DEAD_IMG_URL = "https://arweave.net/RHLYg5wZwpCX3ZwwZYAJTriJo1ZkLB2ruGHbfy6GfJc"


def find_alive_mint_ids(mint_ids: list):
    alive_ids: list = read_json('alive_mint_ids.json')
    return list(filter(lambda mint: mint in alive_ids, mint_ids))
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
    dead_ids = read_json("dead_mint_ids.json")
    for el in data:
        mint = el['mint']
        if mint in mint_ids_to_kill:
            for att in el['metadata']['attributes']:
                if att["trait_type"] == "isAlive":
                    att['value'] = "False"
                el['metadata']['image'] = DEAD_IMG_URL
                write_file(data=el['metadata'], name='change_meta/' + mint)
                if mint not in dead_ids:
                    dead_ids.append(mint)
    write_file(dead_ids, 'data/dead_mint_ids')
    subtract_deads_from_alive(all_ids)


def subtract_deads_from_alive(all_ids: list):
    dead_ids: list = read_json("dead_mint_ids.json")
    alive_ids = []
    for el in all_ids:
        if el not in dead_ids:
            alive_ids.append(el)
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
