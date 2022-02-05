from find import find_alive_mint_ids
from utility import write_file, read_json


def main(holders: dict):
    result = dict()

    holders_stats = dict()
    for value, key in holders.items():
        alive_mints = find_alive_mint_ids(key['mints'])
        info = {
            "Total mints": key['amount'],
            "Alive mints": len(alive_mints)
        }
        holders_stats[value] = info
    result['Holders'] = holders_stats

    total_alive = len(read_json('alive_mint_ids.json'))
    total_dead = len(read_json('dead_mint_ids.json'))
    result['Total info'] = {
        "Total Alive": total_alive,
        "Total Dead": total_dead,
        "All": total_alive + total_dead
    }

    print('writing to a output/holders_stats.json')
    write_file(result, 'output/holders_stats')
