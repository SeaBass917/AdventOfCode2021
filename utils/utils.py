
from os import path
import re

class SevenSegHelper():

    def __init__(self):
        # No initialization required.
        pass

    def print(self, num: int):
        """Print a sevent segment display 
        for a given digit."""
        print(self.to_string(num))
    
    def to_string(self, num: int):
        """Converts a digit to a seven segment string.
        e.g. (0) is: 
        ┌────────┐
        │  ████  │
        │ █    █ │
        │ █    █ │
        │        │
        │ █    █ │
        │ █    █ │
        │  ████  │
        └────────┘
        """
    
        seg_chars = self.num_to_seg(num)

        c_A = '█' if 'a' in seg_chars else ' '
        c_B = '█' if 'b' in seg_chars else ' '
        c_C = '█' if 'c' in seg_chars else ' '
        c_D = '█' if 'd' in seg_chars else ' '
        c_E = '█' if 'e' in seg_chars else ' '
        c_F = '█' if 'f' in seg_chars else ' '
        c_G = '█' if 'g' in seg_chars else ' '

        s = "┌──────────┐\n" 
        s += f"│   {c_A}{c_A}{c_A}{c_A}   │\n"
        s += f"│  {c_B}    {c_C}  │\n"
        s += f"│  {c_B}    {c_C}  │\n"
        s += f"│   {c_D}{c_D}{c_D}{c_D}   │\n"
        s += f"│  {c_E}    {c_F}  │\n"
        s += f"│  {c_E}    {c_F}  │\n"
        s += f"│   {c_G}{c_G}{c_G}{c_G}   │\n"
        s += "└──────────┘\n" 
        return s

    def num_to_seg(self, num: int):
        if num in self._num_to_seg.keys():
            return self._num_to_seg[num]
        else:
            raise ValueError(f"{num} not a valid seven segment display value.")
    
    def seg_to_num(self, seg: str):
        key = str(list(set(seg)).sort())
        if key in self._seg_to_num.keys():
            return self._seg_to_num[key]
        else:
            raise ValueError(f"\"{key}\" not a valid seven segment display key.")

    _num_to_seg = {
        0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg',
    }
    _seg_to_num = {
        'abcefg' : 0,
        'cf' : 1,
        'acdeg' : 2,
        'acdfg' : 3,
        'bcdf' : 4,
        'abdfg' : 5,
        'abdefg' : 6,
        'acf' : 7,
        'abcdefg' : 8,
        'abcdfg' : 9,
    }


class Number():
    """A dumb class used to allow pointers in python.
    """

    def __init__(self, num: int):
        self._val = int(num)

    @staticmethod
    def print_grid(grid: list, base="3.0d"):
        s = ""
        for row in grid:
            for num in (row):
                s += f"%{base}, "%(num._val)
            s = s[:-2] + "\n"
        print(s)

    @staticmethod
    def print_list(it: list, base="3.0d"):
        s = ""
        for num in it:
            s += f"%{base}, "%(num._val)
        print(s[:-2])

def nat_sum(N : int, i = 1):
    """Sum of natural integers from i to N
    i=1 by defualt.
    """
    return int(N * (N-1) / 2) - int(i * (i-1) / 2)

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