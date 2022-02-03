from find import find_mint_ids_by_att, kill_mint_ids, find_alive_mint_ids
from utility import read_json

# # Task 3, 6, 9, 16, 23
metadata = read_json("spw_metadata.json")
all_ids = read_json("ssj_mint_ids.json")
t_type = "Mustache"
t_value = "Mechanical Mustache"

ids_with_att = find_mint_ids_by_att(metadata, t_type, t_value)
print(f"found:{ids_with_att}")

ids_to_kill = find_alive_mint_ids(ids_with_att)
print(f"kill:{ids_to_kill}")

kill_mint_ids(metadata, ids_to_kill, all_ids)
