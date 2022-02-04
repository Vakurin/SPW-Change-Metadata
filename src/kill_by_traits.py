from find import find_mint_ids_by_att, kill_mint_ids, find_alive_mint_ids


# # Task 3, 6, 9, 16, 23
def main(metadata, all_ids):
    print('Enter trait type')
    t_type = input()
    print('Enter trait type')
    t_value = input()

    ids_with_att = find_mint_ids_by_att(metadata, t_type, t_value)
    print(f"found:{ids_with_att}")

    ids_to_kill = find_alive_mint_ids(ids_with_att)
    print(f"kill {len(ids_to_kill)} mints:{ids_to_kill}")

    kill_mint_ids(metadata, ids_to_kill, all_ids)
