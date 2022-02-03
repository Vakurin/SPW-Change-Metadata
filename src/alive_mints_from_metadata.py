from find import find_mint_ids_by_att
from utility import write_file


def find_alive_mint_ids(data):
    alive_mint_ids = find_mint_ids_by_att(data, "isAlive", "True")
    print('writing to a data/alive_mint_ids_by_metadata.json')
    write_file(data=alive_mint_ids, name='data/alive_mint_ids_by_metadata')


# # get correct information from metadata
# metadata = read_json("spw_metadata.json")
# find_alive_mint_ids(metadata)
