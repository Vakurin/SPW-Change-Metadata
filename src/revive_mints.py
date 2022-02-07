import os
from random import sample
from utility import read_json, write_file
from find import subtract_deads_from_alive


def main(all_ids: list):
    print("Choose folder")
    folder_name = input()

    files = os.listdir('../change_meta/' + folder_name)
    print(f'Found {len(files)} mints')

    print('How much should be left in this folder (the rest will be revived)')
    left_number = int(input())

    dead_ids: list = read_json("dead_mint_ids.json")

    for file in sample(files, len(files) - left_number):
        mint = file.split('.')[0]
        print(f"revive mint : {mint}")
        dead_ids.remove(mint)
        os.remove('../change_meta/' + folder_name + '/' + file)
    write_file(dead_ids, 'data/dead_mint_ids')
    subtract_deads_from_alive(all_ids)
