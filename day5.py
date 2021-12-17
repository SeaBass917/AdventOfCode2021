import numpy as np
from utils import utils

def p1(file_path, d_type="Answer"):
    
    with open(file_path) as fp_in:

        chunks = fp_in.read().split("\n\n")

        numbers = [int(num) for num in chunks[0].split(",")]
        boards = [utils.parse_grid(board_str, t=utils.Number) for board_str in chunks[1:]]

        # Loop through the numbers and boards to mark the bingos
        is_winner = False
        for number in numbers:

            # Mark all the boards
            for board in boards:

                # Mark the board
                for row in board:
                    for num in row:
                        if num._val == number:
                            num._val = num._val | MASK

                # Determine if the board is a winner
                
                # ROWS
                for row in board:
                    is_winner = is_winner or is_set_bingo_winner(row)
                
                # COLS
                for col in np.transpose(board):
                    is_winner = is_winner or is_set_bingo_winner(col)

                # # DIAG 1
                # is_winner = is_set_bingo_winner(np.diag(board))

                # # DIAG 2
                # is_winner = is_set_bingo_winner(np.diag(np.flipud(board)))

                # 
                if is_winner:
                    # print(number)
                    # utils.Number.print_grid(board)
                    score_winner = calc_bingo_score(board, number)

                    print(f"{d_type}) {score_winner}")
                    break

            if is_winner: break

        return
        
def p2(file_path, d_type="Answer"):
    
    with open(file_path) as fp_in:

        chunks = fp_in.read().split("\n\n")

        numbers = [int(num) for num in chunks[0].split(",")]
        boards = [utils.parse_grid(board_str, t=utils.Number) for board_str in chunks[1:]]

        # Keep a list of winning boards
        win_table = [ False for _ in boards]

        # Loop through the numbers and boards to mark the bingos
        for number in numbers:
                
            # Mark all the boards
            for i, board in enumerate(boards):
                is_winner = False

                # Mark the board
                for row in board:
                    for num in row:
                        if num._val == number:
                            num._val = num._val | MASK

                # Determine if the board is a winner
                
                # ROWS
                for row in board:
                    is_winner = is_winner or is_set_bingo_winner(row)
                
                # COLS
                for col in np.transpose(board):
                    is_winner = is_winner or is_set_bingo_winner(col)

                # # DIAG 1
                # is_winner = is_set_bingo_winner(np.diag(board))

                # # DIAG 2
                # is_winner = is_set_bingo_winner(np.diag(np.flipud(board)))

                # 
                if is_winner:
                    # print(number)
                    # utils.Number.print_grid(board)
                    # if win_table[i] == False: print(f"Board {i} just won.")
                    
                    win_table[i] = True

                    if all(win_table):

                        score_winner = calc_bingo_score(board, number)

                        print(f"{d_type}) {score_winner}")
                        break

            if all(win_table): break

        return
        

if __name__ == '__main__':

    my_name = utils.get_my_name(__file__)

    p1(f"{my_name}/test1", "Test")
    p1(f"{my_name}/input", "Answer")
    p2(f"{my_name}/test1", "Test")
    p2(f"{my_name}/input", "Answer")


    