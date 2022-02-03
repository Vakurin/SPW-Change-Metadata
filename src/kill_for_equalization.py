import random
from enum import Enum, auto
from collections import defaultdict
from find import find_mint_ids_by_att, find_alive_mint_ids, kill_mint_ids
from utility import read_json


class EqualityOption(Enum):
    TWO_VALUES = auto()
    TOTAL = auto()


def get_mints_after_equalization(data: list, trait_type: str, trait_value_1: str, trait_value_2: str):
    mints_1 = find_alive_mint_ids(find_mint_ids_by_att(data, trait_type, trait_value_1))
    print(f"alive {len(mints_1)} mints {trait_type}:{trait_value_1}")
    mints_2 = find_alive_mint_ids(find_mint_ids_by_att(data, trait_type, trait_value_2))
    print(f"alive {len(mints_2)} mints {trait_type}:{trait_value_2}")

    extra_mints_number: int = abs(len(mints_1) - len(mints_2))
    max_mints = mints_1 if len(mints_1) > len(mints_2) else mints_2

    return random.sample(max_mints, extra_mints_number)


def get_alive_traits(data: list, trait_type: str):
    traits_counter = defaultdict(list)
    for el in data:
        mint = el['mint']
        for att in el['metadata']['attributes']:
            if att['trait_type'] == trait_type and find_alive_mint_ids([mint]):
                traits_counter[att['value']].append(mint)
    return dict(traits_counter)


def get_mints_after_total_equalization(data: list, trait_type: str):
    result_mints = []
    alive_traits = get_alive_traits(data, trait_type)
    min_length = min([len(alive_traits[el]) for el in alive_traits])
    t_values_with_min_mints = [key for key, val in alive_traits.items() if len(val) == min_length]

    for t_value, mints in alive_traits.items():
        print(f"{t_value}:{len(mints)}")
        if t_value not in t_values_with_min_mints:
            result_mints.extend(random.sample(mints, len(mints) - min_length))
    return result_mints


# # Task 7, 14, 21, 28, 24
metadata = read_json("ssj_metadata.json")
all_ids = read_json("ssj_mint_ids.json")
t_type = 'Background'
equality_option = EqualityOption.TWO_VALUES

extra_mints = []
if equality_option == EqualityOption.TWO_VALUES:
    t_value_1 = 'Purple'
    t_value_2 = 'Teal'
    # # compare 2 trait values
    extra_mints = get_mints_after_equalization(metadata, t_type, t_value_1, t_value_2)
elif equality_option == EqualityOption.TOTAL:
    # # compare all trait values
    extra_mints = get_mints_after_total_equalization(metadata, t_type)

print(f"extra mints: {len(extra_mints)} ")
kill_mint_ids(metadata, extra_mints, all_ids)
