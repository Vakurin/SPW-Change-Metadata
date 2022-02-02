import json


def read_json(filename):
    f = open(filename)
    return json.load(f)


def write_file(data, name):
    with open(f'./{name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
