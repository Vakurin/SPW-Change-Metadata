import json
import os

DEAD_IMG_URL = "https://arweave.net/RHLYg5wZwpCX3ZwwZYAJTriJo1ZkLB2ruGHbfy6GfJc"


def read_json(filename):
    f = open(filename)
    return json.load(f)


# def files(folder):
#     return os.listdir(folder)


def create_folder(name):
    os.mkdir("./" + name)
    return "./" + name


def remove_dead_ids(data):
    dead_id = find_mint_ids_to_kill(data, "isAlive", "False")


def find_mint_ids_to_kill(data, att_name, att_value):
    count = 0
    mint_ids = []
    # for every element in json file
    for el in data:
        # for attributes for search
        for att in el['metadata']['attributes']:
            mint = el['mint']
            if (att['trait_type'] == att_name) and (att['value'] == att_value):
                count += 1
                mint_ids.append(mint)
    print(f"Find {count} Attributes {att_name} value {att_value}")
    return mint_ids


def kill_mint_ids(data, mint_ids):
    for el in data:
        mint = el['mint']
        if mint in mint_ids:
            for att in el['metadata']['attributes']:
                if att["trait_type"] == "isAlive":
                    att['value'] = "False"
                el['metadata']['image'] = DEAD_IMG_URL
                write_file(data=el['metadata'], mint_id=mint)


def write_file(data, mint_id):
    with open(f'./change_meta/{mint_id}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


metadata = read_json("data/spw_metadata.json")
ids = find_mint_ids_to_kill(metadata, "Mustache", "Mechanical Mustache")
kill_mint_ids(metadata, ids)
