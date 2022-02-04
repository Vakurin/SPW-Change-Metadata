import json
from enum import Enum, auto
from urllib.request import Request, urlopen

from find import find_alive_mint_ids, kill_mint_ids


class FilterOption(Enum):
    GREATER = auto()
    LESS = auto()


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


def filter_magiceden_metadata(magiceden_metadata: list, value: float, filter_option: FilterOption):
    result = []
    if filter_option == FilterOption.LESS:
        result = list(filter(lambda mint: mint['price'] < value, magiceden_metadata))
    elif filter_option == FilterOption.GREATER:
        result = list(filter(lambda mint: mint['price'] > value, magiceden_metadata))
    return result


def get_mints_ids_from_magiceden_metadata(magiceden_metadata: list):
    result = []
    for el in magiceden_metadata:
        result.append(el['mintAddress'])
    return result


def get_unlisted_mints_ids(listed_ids: list, all_ids: list):
    unlisted_ids = []
    for el in all_ids:
        if el not in listed_ids:
            unlisted_ids.append(el)
    return unlisted_ids

# # Task 2, 8, 15, 22, 25
def main(metadata, collection_name: str, all_ids: list):
    listed_metadata = get_listed_mints_magiceden_metadata(collection_name)
    print(f'Found {len(listed_metadata)} listed items')

    unlisted_ids = get_unlisted_mints_ids(get_mints_ids_from_magiceden_metadata(listed_metadata), all_ids)
    print(f'Found {len(unlisted_ids)} NOT listed items')

    print("Enter price (float)")
    mint_price = float(input())

    print(f"""
Enter a balance option:
    1 - Kill mints with floor price LESS than {mint_price}
    2 - Kill mints with floor price MORE than {mint_price}
    """)
    option = FilterOption.LESS if int(input()) == 1 else FilterOption.GREATER

    filtered_ids = get_mints_ids_from_magiceden_metadata(filter_magiceden_metadata(listed_metadata, mint_price, option))
    print(f'Found {len(filtered_ids)} listed items with FP {option.name} than {mint_price}: {filtered_ids}')

    ids_to_kill = find_alive_mint_ids(unlisted_ids + filtered_ids)
    print(f"kill unlisted and filtered ({len(ids_to_kill)}) mints:{ids_to_kill}")
    kill_mint_ids(metadata, ids_to_kill, all_ids)
