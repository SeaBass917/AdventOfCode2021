import numpy as np
from utils import utils

def p1(file_path, d_type="Answer"):
    
    with open(file_path) as fp_in:

        crab_pos = [int(num) for num in fp_in.read().split(",")]

        delta_map = {}

        for pos_i in crab_pos:
            if pos_i not in delta_map: delta_map[pos_i] = 0
            for pos_j in crab_pos:
                delta = pos_j - pos_i if pos_i < pos_j else pos_i - pos_j
                delta_map[pos_i] += delta

        print(delta_map)

        # Find the arg_min, NOTE: unrolling the first loop
        arg_min, arg_min_val = delta_map.popitem()
        for position, val in delta_map.items():
            if val < arg_min_val:
                arg_min_val = val
                arg_min = position
        
        print(f"{d_type}) Position: {arg_min} | Fuel Cost: {arg_min_val}")

        return
        
def p2(file_path, d_type="Answer"):
        return

if __name__ == '__main__':

    my_name = utils.get_my_name(__file__)

    p1(f"{my_name}/test1", "Test")
    # p1(f"{my_name}/input", "Answer")
    # p2(f"{my_name}/test1", "Test")
    # p2(f"{my_name}/input", "Answer")


    