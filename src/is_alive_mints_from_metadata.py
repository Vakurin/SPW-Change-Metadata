from find import find_mint_ids_by_att
from utility import write_file
from enum import Enum, auto


class Option(Enum):
    ALIVE = auto()
    DEAD = auto()


def find_alive_mint_ids(data):
    alive_mint_ids = find_mint_ids_by_att(data, "isAlive", "True")
    print('writing to a output/alive_mint_ids_by_metadata.json')
    write_file(data=alive_mint_ids, name='output/alive_mint_ids_by_metadata')


def find_dead_mint_ids(data):
    dead_mint_ids = find_mint_ids_by_att(data, "isAlive", "False")
    print('writing to a output/dead_mint_ids_by_metadata.json')
    write_file(data=dead_mint_ids, name='output/dead_mint_ids_by_metadata')


# # get correct information from metadata
def main(metadata):
    find_alive_mint_ids(metadata)
    find_dead_mint_ids(metadata)
