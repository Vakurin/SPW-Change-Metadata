from find import find_mint_ids_by_att, kill_mint_ids
from utility import read_json

metadata = read_json("data/spw_metadata.json")
all_ids = read_json("data/ssj_mint_ids.json")

ids_to_kill = find_mint_ids_by_att(metadata, "Mustache", "Mechanical Mustache")
print(ids_to_kill)
kill_mint_ids(metadata, ids_to_kill, all_ids)
