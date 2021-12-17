
from os import path
import re

class Number():
    """A dumb class used to allow pointers in python.
    """

    def __init__(self, num: int):
        self._val = int(num)

    @staticmethod
    def print_grid(grid: list):
        for row in grid:
            for num in row:
                print("%8.0x, "%(num._val), end="")
            print()

    @staticmethod
    def print_list(it: list):
        for num in it:
            print("%8.0x, "%(num._val), end="")
        print()


def base_cnvrt(digits, base=2):
    """Converts a number to decimal from any base.

    Input
    -------
    num : list[int]
        e.g. [0, 1, 0, 1, 0, 0, 1]
    
    Returns
    --------
    dec : int
        [0, 1, 0, 1, 0, 0, 1] in base 2 → 41
    """

    s = 0

    exp = len(digits) - 1

    for digit in digits:
        s += digit * pow(base, exp)
        exp -= 1

    return s

def get_my_name(full_path):
    """Returns the file name, provided a path.

    Input
    -------
    path : str
        Path. e.g. "C:/.../.../.../myfile.py"
    
    Returns
    --------
    filename : str
        "myfile"
    """
    return path.basename(full_path)[:-3]

def parse_grid(grid_str: str, t=str):
    """Converts a grid string into a grid.

    Input
    ------
    grid_str : str
        "1 2 3 4 5 6
         6 7 8 9 0 1
         2 3 4 5 6 7"
    
    t : type
        Optional typcasting for the values in the grid.

    Returns
    -------
        [[1 2 3 4 5 6]
         [6 7 8 9 0 1]
         [2 3 4 5 6 7]]
    """
    # remove duplicate spaces
    grid_str = re.sub(r" +", " ", grid_str)
    return [[t(ele) for ele in row.strip().split(" ")] for row in grid_str.split("\n")]