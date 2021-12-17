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
    
    with open(file_path) as fp_in:

        lines = [[int(c) for c in line] for line in fp_in.read().split("\n")]
        lines = np.array(lines)

        i = 0
        while 1 < len(lines):
            lines_t = np.transpose(lines)
            
            bins = {}

            for j, digit in enumerate(lines_t[i]):
                if digit not in bins.keys():
                    bins[digit] = []
                
                bins[digit].append(lines[j])

            digit_max_cnt = -1
            for v in bins.values():
                if digit_max_cnt < len(v):
                    digit_max_cnt = len(v)
                    lines = v

            i += 1

        print(lines[0])
        print(utils.base_cnvrt(lines[0]))
        

        # print(f"{type} 2) Gamma: {gamma}, Epsilon: {epsilon}, P: {pow_con}")
        return


if __name__ == '__main__':

    my_name = utils.get_my_name(__file__)

    p1(f"{my_name}/test1", "Test")
    p1(f"{my_name}/input", "Answer")
    p2(f"{my_name}/test1", "Test")
    p2(f"{my_name}/input", "Answer")

    """
    This is a trivial problem if you grep the dataset.
    I realised this after I wrote most of the problem in here, so I'll keep the code.
    But just grep this

    Grep for:
    ^0 ^1
    ^10 ^11
    ^100 ^101
    ...



    2,397
    673     X
    ---------
    1,613,181

    2799       (101011101111)
    1601  X    (011001000001)
    -------
    4481199
    """

    