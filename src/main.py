# metadata = read_json("data/spw_metadata.json")
# names = read_json("data/names_to_kill.json")
# ids = find_mint_ids_by_name(metadata, names)
# kill_mint_ids(metadata, ids)


def main():
    print("Starting SPW program: ")
    print("""
    Choose what you want to do:
    1 - Kill by traits
    2 - Kill by names
    3 - Stats how many cats and dogs alive
    4 - Check unique holders
    5 - 
    """)
    while True:
        print("Enter number:")
        program_num = int(input())
        if program_num > 0:
            break
    
    if program_num == 1:
        print("")
    elif program_num == 2:
        pass

main()