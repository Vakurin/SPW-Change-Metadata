import json


# os.mkdir('../change_meta/')

def read_json(filename):
    f = open('../data/' + filename)
    return json.load(f)


def read_updated_json(filename):
    f = open('../need_updating/' + filename)
    return json.load(f)


def write_file(data, name):
    with open(f'../{name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_img_url(day: str):
    img_urls: list = read_json('from17.json')
    for url in img_urls:
        name: str = url['name']
        if name.split('.')[0] == day:
            return url['link']
    raise SystemExit('Not found img with this name')