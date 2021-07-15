# Simple Sudoko
# Made by @Yazzuk
# No license I guess idk how this all works ;)

# Sudoko rules for my reference:
'''
Every square has to contain a single number
Only the numbers from 1 through to 9 can be used
Each 3×3 box can only contain each number from 1 to 9 once
Each vertical column can only contain each number from 1 to 9 once
Each horizontal row can only contain each number from 1 to 9 once
'''
import numpy as np
import random

row_count = 9
col_count = 9
valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

grid = np.zeros((col_count, row_count), dtype="int16")


'''
    Okay so, to get a random board, we need to populate it first, this code
    block below just fills up the array of zeros with a valid number.

'''
def populate_board(board):
    for col in range(col_count):
        valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for row in range(row_count):
            grid[row][col] = random.choice(valid_numbers)
            for i in valid_numbers:
                if i == grid[row][col]:
                    valid_numbers.remove(i)
'''
    The approach I'm trying here is to get the number of dupes in a given row,
    since the numbers in the columns dont have a dupe, as can be seen in the
    function above.
'''

def set_board(board):
    valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in range(9):
        for col in range(9):
            for i in board[col]:
                pass

'''
    In this function next, I will try to get the dupes in the given array/board,
    and check what numbers are n > 1, and what n < 0, that way we get what dupes
    are in the board, basically sorting the array so it has the winning -
    combination, and when the board is valid, we just remove random numbers in
    it.
'''





populate_board(grid)
set_grid = set_board(grid)
print(grid)
print(set_grid)
