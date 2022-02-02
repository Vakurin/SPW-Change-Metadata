from utility import read_json
import json

def metaboos_json(file):
    data = read_json(file)
    for el in data:
        el['new_uri'] = el["link"]
        without_json = el['name'].split('.')[0]
        el['mint_account'] = without_json
        del el["link"]
        del el["name"]
    print(data)
    write_file(data, "update-metaboss")

def write_file(data, name, path=None):
    with open(f'./{name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

metaboos_json("./data/change-it.json")