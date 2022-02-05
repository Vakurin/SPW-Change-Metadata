import change_metaboss
import holders_stats
import is_alive_mints_from_metadata
import kill_by_holder_address
import kill_by_names
import kill_by_price
import kill_by_traits
import kill_for_balancing
import kill_listed_or_unlisted
import kill_with_diff_traits_per_holder
from utility import read_json

metadata = read_json("ssj_metadata.json")
all_ids = read_json("ssj_mint_ids.json")
holders = read_json('ssj_holders.json')
collection_name = 'solana_samurai_journey'

functions = {
    1: lambda: kill_by_traits.main(metadata, all_ids),
    2: lambda: kill_by_names.main(metadata, all_ids),
    3: lambda: kill_for_balancing.main(metadata, all_ids),
    4: lambda: kill_by_holder_address.main(metadata, holders, all_ids),
    5: lambda: kill_with_diff_traits_per_holder.main(metadata, holders, all_ids),
    6: lambda: kill_by_price.main(metadata, collection_name, all_ids),
    7: lambda: kill_listed_or_unlisted.main(metadata, collection_name, all_ids),
    8: lambda: change_metaboss.main("arweave_output.json"),
    9: lambda: kill_for_balancing.get_mints_after_balancing(metadata, 'Type', 'Dog', 'Cat'),
    10: lambda: holders_stats.main(holders),
    11: lambda: is_alive_mints_from_metadata.main(metadata),
}


def switch_function(argument):
    func = functions.get(argument, lambda: print("Invalid argument"))
    return func()


def main():
    print("""
Starting SPW program: 
Choose what you want to do:
    1 - Kill by traits
    2 - Kill by names
    3 - Kill for balance
    4 - Kill if holder address contains number
    5 - Kill if holder has mints with different trait values
    6 - Kill by floor price
    7 - Kill listed/unlisted mints
    8 - Update Metaboss file
    9 - Stats how many cats and dogs alive
    10 - Stats for holders
    11 - Update (alive/dead) _mint_ids_by_metadata.json for checking
    """)

    print("Enter number:")
    program_num = int(input())

    switch_function(program_num)


main()
