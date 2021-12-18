import numpy as np
from utils import utils

def p1(file_path, d_type="Answer"):
    
    with open(file_path) as fp_in:

        fishies = [utils.Number(num) for num in fp_in.read().split(",")]

        DAYS_TOTAL = 80
        DAYS_SPAWN = 7

        for i_day in range(DAYS_TOTAL):

            num_fish_spawning = 0
            for fish in fishies:
                age = fish._val
                if age == 0:
                    num_fish_spawning += 1
                    fish._val = DAYS_SPAWN - 1
                else:
                    fish._val = age - 1

            for _ in range(num_fish_spawning):
                fishies.append(utils.Number(8))

            # utils.Number.print_list(fishies, base="d")

        print(f"{d_type}) {len(fishies)}")

        return
        
def p2(file_path, d_type="Answer"):
    
    with open(file_path) as fp_in, open("test.csv", mode="w") as fp_out:

        fishies = [int(num) for num in fp_in.read().split(",")]

        DAYS_TOTAL = 256
        DAYS_SPAWN = 7
        DAYS_SPAWN_NEW = 9

        # Create a map to represent the num fish in each spawning state
        # Initialize it using the given data
        spawn_map = { k: 0 for k in range(DAYS_SPAWN_NEW)}
        for age in fishies:
            spawn_map[age] += 1

        num_fishies_spawning = 0
        for i_day in range(DAYS_TOTAL):
    
            # spawn_map[0] = spawn_map[1]
            # spawn_map[1] = spawn_map[2]
            # spawn_map[2] = spawn_map[3]
            # spawn_map[3] = spawn_map[4]
            # spawn_map[4] = spawn_map[5]
            # spawn_map[5] = spawn_map[6]
            # spawn_map[6] = spawn_map[7]
            # spawn_map[7] = spawn_map[8]
            
            # spawn_map[8] = spawn_map[0]
            for i in range(DAYS_SPAWN_NEW-1):
                spawn_map[i] = spawn_map[i+1]

            spawn_map[DAYS_SPAWN_NEW-1] = num_fishies_spawning
            spawn_map[DAYS_SPAWN-1] += num_fishies_spawning

            num_fishies_spawning = spawn_map[0]

        num_fishies = sum(spawn_map.values())

        print(f"{d_type}) {num_fishies}")

        return

if __name__ == '__main__':

    my_name = utils.get_my_name(__file__)

    p1(f"{my_name}/test1", "Test")
    p1(f"{my_name}/input", "Answer")
    p2(f"{my_name}/test1", "Test")
    p2(f"{my_name}/input", "Answer")


    