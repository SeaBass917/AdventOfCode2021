
# [0, 50] stars


def p1(file_path):
    
    with open(file_path) as fp_in:

        lines = [line.split() for line in fp_in.read().split("\n")]

        pos_x = 0
        pos_y = 0
        pos_z = 0

        for dir, n in lines:
            dir = dir.lower()
            n = int(n)
            if dir == "forward":
                pos_x += n
            elif dir == "down":
                pos_z += n
            elif dir == "up":
                pos_z -= n
            else:
                print(f"huh?? what's {dir}")
        prod = pos_x*pos_z
        print(f"Answer 1: (pos_x, pos_z) ({pos_x}x{pos_z}) = {prod}")

def p2(file_path):
    
    with open(file_path) as fp_in:

        lines = [line.split() for line in fp_in.read().split("\n")]

        pos_x = 0
        pos_aim = 0
        pos_z = 0

        for dir, n in lines:
            dir = dir.lower()
            n = int(n)
            if dir == "forward":
                pos_x += n
                pos_z += pos_aim * n
            elif dir == "down":
                pos_aim += n
            elif dir == "up":
                pos_aim -= n
            else:
                print(f"huh?? what's {dir}")
        prod = pos_x*pos_z
        print(f"Answer 2: (pos_x, pos_z) ({pos_x}x{pos_z}) = {prod}")


if __name__ == '__main__':
    # p1("day2/data/test1")
    p1("day2/data/input")
    p2("day2/data/input")
    # p2("day2/data/test1")
    