import random
from enum import Enum, auto
from utility import read_json, write_file
from find import kill_mint_ids, get_holders_with_alive_mints


class Option(Enum):
    STARTS = auto()
    ENDS = auto()


def get_holders_with_number(holders: dict, option: Option):
    result_holders = dict()
    for key, value in holders.items():
        if option == option.STARTS and key[0].isdigit():
            result_holders[key] = value
        elif option == option.ENDS and key[len(key) - 1].isdigit():
            result_holders[key] = value

    return result_holders


def get_mints_from_holders(holders: dict, mints_number: int):
    result_mints = []
    for holder, mints in holders.items():
        result_mints.extend(random.sample(mints, mints_number))
    return result_mints


# # Task 19, 27
metadata = read_json("ssj_metadata.json")
holders_with_all_mints = read_json('ssj_holders.json')
all_ids = read_json("ssj_mint_ids.json")
mints_per_holder = 1
address_option = Option.ENDS

holder_with_alive_mints = get_holders_with_alive_mints(mints_per_holder, holders_with_all_mints)
print(f"found {len(holder_with_alive_mints)} holders with >={mints_per_holder} alive mints")

dead_holders = get_holders_with_number(holder_with_alive_mints, address_option)
print(f"found {len(dead_holders)} holders addresses {address_option.name} with number")

ids_to_kill = get_mints_from_holders(dead_holders, mints_per_holder)
print(f"extra mints: {len(ids_to_kill)} ")

kill_mint_ids(metadata, ids_to_kill, all_ids)
