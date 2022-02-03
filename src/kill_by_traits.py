from find import find_mint_ids_by_att, kill_mint_ids, find_alive_mint_ids
from utility import read_json

metadata = read_json("data/spw_metadata.json")
all_ids = read_json("data/ssj_mint_ids.json")

ids_with_att = find_mint_ids_by_att(metadata, "Mustache", "Mechanical Mustache")
print(f"found:{ids_with_att}")
ids_to_kill = find_alive_mint_ids(ids_with_att)
print(f"kill:{ids_to_kill}")
kill_mint_ids(metadata, ids_to_kill, all_ids)
