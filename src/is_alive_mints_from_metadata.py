from find import find_mint_ids_by_att
from utility import write_file


# # get correct information from metadata

def find_alive_mint_ids(data):
    alive_mint_ids = find_mint_ids_by_att(data, "isAlive", "True")
    print('writing to a data/alive_mint_ids_by_metadata.json')
    write_file(data=alive_mint_ids, name='output/alive_mint_ids_by_metadata')


def find_dead_mint_ids(data):
    dead_mint_ids = find_mint_ids_by_att(data, "isAlive", "False")
    print('writing to a data/dead_mint_ids_by_metadata.json')
    write_file(data=dead_mint_ids, name='output/dead_mint_ids_by_metadata')
