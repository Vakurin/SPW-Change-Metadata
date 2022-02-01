from asyncore import read
import json
import os
from sre_parse import parse


### 1. Cначала нужно обновить метаданные
### 2. Загрузить файлы 
### 3. Потом уже сам файл

DEAD_URL = "https://arweave.net/RHLYg5wZwpCX3ZwwZYAJTriJo1ZkLB2ruGHbfy6GfJc"

def read_json(filename):
    f = open(filename)
    data = json.load(f)
    return data

# def files(folder):
#     return os.listdir(folder)


def create_folder(name):
    os.mkdir("./" + name)
    return "./" + name

def remove_dead_ids(data):
    dead_id = find_attributes(data, "isAlive", "False", kill=False)


def find_attributes(data, att_name, att_value, kill=False):
    count = 0
    mint_ids = []
    # for every element in json file
    for el in data:
        # for attributes for search
        for att in el['metadata']['attributes']:
            if (att['trait_type'] == att_name) & (att['value'] == att_value) :
                id = el['mint']
                count += 1
                mint_ids.append(id)
                ### Change Attribute
                if kill:
                    if(att["trait_type"] == "isAlive"):
                        att['value'] = "False"
                    el['metadata']['image'] = DEAD_URL

                    # Write file
                    write_file(data=el['metadata'], mint_id=id)
    print(f"Find {count} Attributes {att_name} value {att_value}")
    return mint_ids
    

def write_file(data, mint_id):
    with open(f'./change_meta/{mint_id}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


data = read_json("data/spw_metadata.json")
ids = find_attributes(data, "isAlive", "True", kill=True)


# print(read_json("data/ssj_metadata.json"))