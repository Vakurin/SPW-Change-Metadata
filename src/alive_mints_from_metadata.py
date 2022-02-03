from find import find_mint_ids_by_att
from utility import read_json, write_file


def find_alive_mint_ids(data):
    alive_mint_ids = find_mint_ids_by_att(data, "isAlive", "True")
    write_file(data=alive_mint_ids, name='data/alive_mint_ids_by_metadata')


# # get correct information from metadata
metadata = read_json("data/spw_metadata.json")
find_alive_mint_ids(metadata)
