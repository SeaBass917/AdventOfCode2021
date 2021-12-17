import numpy as np
from utils import utils

def p1(file_path, d_type="Answer"):
    
    with open(file_path) as fp_in:

        coord_pairs = [[[int(s) for s in coord.split(",")] for coord in line.split(" -> ")] for line in fp_in.read().split("\n")]

        # Make the grid a square
        grid_len = max(np.array(coord_pairs).flatten()) + 1
        grid = np.zeros((grid_len, grid_len), dtype=int)

        for (x1, y1), (x2, y2) in coord_pairs:
            
            # Draw the line
            if(x1 == x2):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[y][x1] += 1

            if(y1 == y2):
                for x in range(min(x1, x2), max(x1, x2)+1):
                    grid[y1][x] += 1

        count = 0
        for num in grid.flatten():
            if 1 < num:
                count += 1
        
        print(f"{d_type}) {count}")
        return
        
def p2(file_path, d_type="Answer"):
    
    with open(file_path) as fp_in:

        coord_pairs = [[[int(s) for s in coord.split(",")] for coord in line.split(" -> ")] for line in fp_in.read().split("\n")]

        # Make the grid a square
        grid_len = max(np.array(coord_pairs).flatten()) + 1
        grid = np.zeros((grid_len, grid_len), dtype=int)

        for (x1, y1), (x2, y2) in coord_pairs:

            slope_n = (y2 - y1)
            slope_d = (x2 - x1)
            
            # Draw the line
            if slope_d == 0:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[y][x1] += 1

            elif slope_n == 0:
                for x in range(min(x1, x2), max(x1, x2)+1):
                    grid[y1][x] += 1

            else:

                slope = slope_n / slope_d
                
                # We always draw left to righjt, 
                # so make sure starting y is right
                y = y2 if x2 < x1 else y1

                for i, x in enumerate(range(min(x1, x2), max(x1, x2)+1)):
                    grid[int(y+i*slope)][x] += 1

        count = 0
        for num in grid.flatten():
            if 1 < num:
                count += 1
        
        print(f"{d_type}) {count}")
        return
        
        

if __name__ == '__main__':

    my_name = utils.get_my_name(__file__)

    p1(f"{my_name}/test1", "Test")
    p1(f"{my_name}/input", "Answer")
    p2(f"{my_name}/test1", "Test")
    p2(f"{my_name}/input", "Answer")


    