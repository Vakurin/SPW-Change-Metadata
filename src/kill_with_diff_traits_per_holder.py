import random

from find import kill_mint_ids, get_mint_att_dict, get_holders_with_alive_mints
from utility import read_json


# get mints if holder has mints with different trait values
def get_extra_mints_from_holders(holders: dict, mints_number: int, mint_att: dict):
    result_mints = []
    for holder, mints in holders.items():
        temp = mint_att.get(mints[0])
        for mint in mints:
            if mint_att.get(mint) != temp:
                result_mints.extend(random.sample(mints, mints_number))
                break
    return result_mints


# # Task 4, 12?
metadata = read_json("data/ssj_metadata.json")
holders_with_all_mints = read_json('data/ssj_holders.json')
all_ids = read_json("data/ssj_mint_ids.json")
t_type = 'Background'
mints_per_holder = 1

holder_with_alive_mints = get_holders_with_alive_mints(mints_per_holder, holders_with_all_mints)
print(f"found {len(holder_with_alive_mints)} holders with >={mints_per_holder} alive mints")

mint_att_dict = get_mint_att_dict(metadata, t_type)

ids_to_kill = get_extra_mints_from_holders(holder_with_alive_mints, mints_per_holder, mint_att_dict)
print(f"kill:{ids_to_kill}")

# kill_mint_ids(metadata, ids_to_kill, all_ids)
