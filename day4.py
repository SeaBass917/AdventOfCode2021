import numpy as np
from utils import utils

def p1(file_path, type="Answer"):
    
    with open(file_path) as fp_in:

        lines = [[int(c) for c in line] for line in fp_in.read().split("\n")]

        lines = np.array(lines)

        lines_t = np.transpose(lines)

        gamma = []
        epsilon = []
        for col in lines_t:
            maj = int(np.median(col)) # hehe
            gamma.append(maj) 
            epsilon.append(0x1 ^ maj)

        # print(f"Gamma: {gamma}, Epsilon: {epsilon}")
        gamma = utils.base_cnvrt(gamma)
        epsilon = utils.base_cnvrt(epsilon)

        pow_con = gamma * epsilon
        print(f"{type} 1) Gamma: {gamma}, Epsilon: {epsilon}, P: {pow_con}")

        return
        
def p2(file_path, type="Answer"):
    return


if __name__ == '__main__':

    my_name = utils.get_my_name(__file__)

    p1(f"{my_name}/test1", "Test")
    p1(f"{my_name}/input", "Answer")
    p2(f"{my_name}/test1", "Test")
    p2(f"{my_name}/input", "Answer")


    