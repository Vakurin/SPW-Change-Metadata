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
    print("""
Enter a option:
    1 - Get info about ALIVE mints from metadata 
    2 - Get info about DEAD mints from metadata
    """)

    option = Option.ALIVE if int(input()) == 1 else Option.DEAD

    if option == Option.ALIVE:
        find_alive_mint_ids(metadata)
    elif option == Option.DEAD:
        find_dead_mint_ids(metadata)
