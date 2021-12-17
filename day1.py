
# [0, 50] stars


def p1():
    
    with open("day1/data/input") as fp_in:

        lines = fp_in.read().split("\n")

        count_larger = 0

        x_prev = int(lines.pop(0))
        for line in lines:
            if x_prev < int(line):
                count_larger+=1
                # print(f"{line} (Increased)")
            else:
                # print(f"{line} (d)")
                pass
            x_prev = int(line)

        print(f"Answer 1: {count_larger}")

def p2(file_path):
    
    with open(file_path) as fp_in:

        lines = [int(x) for x in fp_in.read().split("\n")]

        count_larger = 0

        x_prev = lines[0] + lines[1] + lines[2]
        for i in range(2, len(lines)-1):
            
            x = lines[i-1] + lines[i] + lines[i+1]
            
            if x_prev < x:
                count_larger+=1
                # print(f"{x} (Increased)")
            else:
                # print(f"{x} (d)")
                pass
            x_prev = x

        print(f"Answer 2: {count_larger}")

if __name__ == '__main__':
    p1()
    p2("day1/data/input")
    p2("day1/data/test2")
    