import numpy as np
from utils import utils

def p1(file_path, d_type="Answer"):
    
    with open(file_path) as fp_in:

        crab_pos = [int(num) for num in fp_in.read().split(",")]

        print(f"{d_type}) Position: {arg_min} | Fuel Cost: {arg_min_val}")

        return
        
def p2(file_path, d_type="Answer"):
    return
        

if __name__ == '__main__':

    my_name = utils.get_my_name(__file__)

    ss = utils.SevenSegHelper()

    for i in range(10):
        ss.print(i)

    # p1(f"{my_name}/test1", "Test")
    # p1(f"{my_name}/input", "Answer")
    # p2(f"{my_name}/test1", "Test")
    # p2(f"{my_name}/input", "Answer")


    