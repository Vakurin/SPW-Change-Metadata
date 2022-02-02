from utility import read_json
from find import find_mint_ids_by_name, kill_mint_ids

metadata = read_json("data/spw_metadata.json")
names = read_json("data/names_to_kill.json")
all_ids = read_json("data/ssj_mint_ids.json")

ids_to_kill = find_mint_ids_by_name(metadata, names)
print(ids_to_kill)
kill_mint_ids(metadata, ids_to_kill, all_ids)
