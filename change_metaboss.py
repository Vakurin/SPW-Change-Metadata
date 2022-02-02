from utility import read_json
from utility import write_file


def metaboss_json(file):
    data = read_json(file)
    for el in data:
        el['new_uri'] = el["link"]
        without_json = el['name'].split('.')[0]
        el['mint_account'] = without_json
        del el["link"]
        del el["name"]
    print(data)
    write_file(data, "update-metaboss")


metaboss_json("data/metaboss-change-it.json")
