import json
import os
import datetime


# os.mkdir('../change_meta/')

def read_json(filename):
    f = open('../data/' + filename)
    return json.load(f)


def write_file(data, name):
    with open(f'../{name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
