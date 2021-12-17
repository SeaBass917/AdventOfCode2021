
from os import path

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
