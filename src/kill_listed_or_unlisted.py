from enum import Enum, auto
from find import find_alive_mint_ids, kill_mint_ids, get_mints_ids_from_magiceden_metadata, \
    get_listed_mints_magiceden_metadata, subtract_lists


class MarketOption(Enum):
    LISTED = auto()
    UNLISTED = auto()


# # Task 17, 20
def main(metadata, collection_name: str, all_ids: list):
    listed_ids = get_mints_ids_from_magiceden_metadata(get_listed_mints_magiceden_metadata(collection_name))
    print(f'Found {len(listed_ids)} listed items')

    unlisted_ids = subtract_lists(listed_ids, all_ids)
    print(f'Found {len(unlisted_ids)} NOT listed items')

    print(f"""
Enter a balance option:
    1 - Kill listed mints
    2 - Kill unlisted mints
    """)
    option = MarketOption.LISTED if int(input()) == 1 else MarketOption.UNLISTED

    ids_to_kill = []
    if option == MarketOption.LISTED:
        ids_to_kill = find_alive_mint_ids(listed_ids)
    elif option == MarketOption.UNLISTED:
        ids_to_kill = find_alive_mint_ids(unlisted_ids)

    print(f"kill {option.name} ({len(ids_to_kill)}) mints:{ids_to_kill}")
    kill_mint_ids(metadata, ids_to_kill, all_ids)
