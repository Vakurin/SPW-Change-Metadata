import json
from urllib.request import Request, urlopen


def get_listed_mints():
    mints = []
    counter = 0
    while True:
        url = f'https://api-mainnet.magiceden.io/rpc/getListedNFTsByQuery?q={{"$match":' \
              f'{{"collectionSymbol":"solana_samurai_journey"}},"$skip":{counter}}}'
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        results: list = json.loads(web_byte.decode('utf-8'))['results']
        counter += 20
        mints.extend(results)
        if len(results) == 0:
            break
    print(f'Found {len(mints)} listed items')


get_listed_mints()
