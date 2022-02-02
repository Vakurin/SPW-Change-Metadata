from utility import read_json
from find import kill_mint_ids
import random


def get_holders_with_alive_mints(mints_number: int, holders: dict):
    alive_ids: list = read_json('data/alive_mint_ids.json')
    holders_mints = dict()
    for value, key in holders.items():
        alive_mints = list(filter(lambda mint: mint in alive_ids, key['mints']))
        if len(alive_mints) > mints_number:
            holders_mints[value] = alive_mints
    # write_file(holders, 'test')
    return holders_mints


def get_mint_att_dict(data: list, att_name):
    mint_att_dict = dict()
    for el in data:
        mint = el['mint']
        for att in el['metadata']['attributes']:
            if att['trait_type'] == att_name:
                mint_att_dict[mint] = att
    return mint_att_dict


# get mints if holder has mints with different trait values
def get_mints_from_holders(holders: dict, mints_number: int, mint_att: dict):
    result_mints = []
    for holder, mints in holders.items():
        temp = mint_att.get(mints[0])
        for mint in mints:
            if mint_att.get(mint) != temp:
                result_mints.extend(random.sample(mints, mints_number))
                break
    return result_mints


metadata = read_json("data/ssj_metadata.json")
holders = read_json('data/ssj_holders.json')
all_ids = read_json("data/ssj_mint_ids.json")
trait = 'Background'
mints_per_holder = 1

ids_to_kill = get_mints_from_holders(get_holders_with_alive_mints(mints_per_holder, holders),
                                     mints_per_holder,
                                     get_mint_att_dict(metadata, trait))
print(ids_to_kill)
kill_mint_ids(metadata, ids_to_kill, all_ids)
