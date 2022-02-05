import json


# # format to correct struct
def main():
    f = open('../metaboss/arweave.json')
    data = json.load(f)
    for el in data:
        el['new_uri'] = el["link"]
        without_json = el['name'].split('.')[0]
        el['mint_account'] = without_json
        del el["link"]
        del el["name"]
    print('writing to metaboss/metaboss.json', data)
    with open(f'../metaboss/metaboss.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
