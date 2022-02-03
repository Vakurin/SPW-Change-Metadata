from utility import read_json
from find import kill_mint_ids, find_mint_ids_by_att, find_alive_mint_ids
import random


def get_mints_after_equation(data: list, trait_type: str, trait_value_1: str, trait_value_2: str):
    mints_1 = find_alive_mint_ids(find_mint_ids_by_att(data, trait_type, trait_value_1))
    print(f"alive {len(mints_1)} mints {trait_type}:{trait_value_1}")
    mints_2 = find_alive_mint_ids(find_mint_ids_by_att(data, trait_type, trait_value_2))
    print(f"alive {len(mints_2)} mints {trait_type}:{trait_value_2}")

    extra_mints_number: int = abs(len(mints_1) - len(mints_2))
    max_mints = mints_1 if len(mints_1) > len(mints_2) else mints_2

    return random.sample(max_mints, extra_mints_number)


# task 7, 14, 21, 28, 24(need update code)
metadata = read_json("data/ssj_metadata.json")
holders = read_json('data/ssj_holders.json')
all_ids = read_json("data/ssj_mint_ids.json")
t_type = 'Background'
t_value_1 = 'Purple'
t_value_2 = 'Green'

extra_mints = get_mints_after_equation(metadata, t_type, t_value_1, t_value_2)
print(f"extra mints: {len(extra_mints)} ")
kill_mint_ids(metadata, extra_mints, all_ids)
