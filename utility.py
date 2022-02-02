import json


def read_json(filename):
    f = open(filename)
    return json.load(f)
