from utility import read_json
from utility import write_file

DEAD_IMG_URL = "https://arweave.net/RHLYg5wZwpCX3ZwwZYAJTriJo1ZkLB2ruGHbfy6GfJc"


# extra function to find from *_metadata.json
def find_alive_mint_ids(data):
    alive_mint_ids = find_mint_ids_by_att(data, "isAlive", "True")
    write_file(data=alive_mint_ids, name='data/alive_mint_ids_by_metadata')


def find_mint_ids_by_att(data, att_name, att_value):
    count = 0
    mint_ids = []
    # for every element in json file
    for el in data:
        mint = el['mint']
        # for attributes for search
        for att in el['metadata']['attributes']:
            if (att['trait_type'] == att_name) and (att['value'] == att_value):
                count += 1
                mint_ids.append(mint)
    print(f"Find {count} Attributes {att_name} value {att_value}")
    return mint_ids


def find_mint_ids_by_name(data, names_to_kill):
    count = 0
    mint_ids = []
    for el in data:
        mint = el['mint']
        name = el['metadata']['name']
        if int(name.split('#', 1)[1]) in names_to_kill:
            count += 1
            mint_ids.append(mint)
    print(f"Find {count} Names")
    return mint_ids


def kill_mint_ids(data, mint_ids_to_kill):
    dead_ids = read_json("data/dead_mint_ids.json")
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
    subtract_deads_from_alive()


def subtract_deads_from_alive():
    all_ids = read_json("data/spw_mint_ids.json")
    dead_ids = read_json("data/dead_mint_ids.json")
    alive_ids = []
    for el in all_ids:
        if el not in dead_ids:
            alive_ids.append(el)
    write_file(alive_ids, 'data/alive_mint_ids')


# # get alive mint ids from metadata
# metadata = read_json("data/spw_metadata.json")
# find_alive_mint_ids(metadata)

# # kill from traits
# metadata = read_json("data/spw_metadata.json")
# ids = find_mint_ids_by_att(metadata, "Mustache", "Mechanical Mustache")
# kill_mint_ids(metadata, ids)

# # kill from names
metadata = read_json("data/spw_metadata.json")
names = read_json("data/names_to_kill.json")
ids = find_mint_ids_by_name(metadata, names)
kill_mint_ids(metadata, ids)
