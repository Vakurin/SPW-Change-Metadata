from find import kill_mint_ids, find_alive_mint_ids
from utility import read_updated_json


def find_mint_ids_by_name(data, names_to_kill):
    count = 0
    mint_ids = []
    for el in data:
        mint = el['mint']
        name = el['metadata']['name']
        # if int(name.split('#', 1)[1]) in names_to_kill:
        #     count += 1
        #     mint_ids.append(mint)
        if mint in names_to_kill:
            count += 1
            mint_ids.append(mint)
    print(f"Find {count} Names")
    return mint_ids


# # Task 13
def main(metadata, all_ids):
    names = read_updated_json("names_to_kill.json")

    ids_with_names = find_mint_ids_by_name(metadata, names)
    print(f"found:{ids_with_names}")

    ids_to_kill = find_alive_mint_ids(ids_with_names)
    print(f"kill {len(ids_to_kill)} mints:{ids_to_kill}")

    kill_mint_ids(metadata, ids_to_kill, all_ids)
