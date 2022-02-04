from utility import read_json
from utility import write_file


# # format to correct struct
def main(file):
    data = read_json(file)
    for el in data:
        el['new_uri'] = el["link"]
        without_json = el['name'].split('.')[0]
        el['mint_account'] = without_json
        del el["link"]
        del el["name"]
    print('writing to output/update_metaboss.json', data)
    write_file(data, "output/update_metaboss")
