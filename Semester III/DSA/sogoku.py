import numpy as np
count = 0
str_inp = '''0 0 3 4 0 0 0 8 9
0 0 6 7 8 9 0 2 3
0 8 0 0 2 3 4 5 6
0 0 4 0 6 5 0 9 7
0 6 0 0 9 0 0 1 4
0 0 7 2 0 4 3 6 5
0 3 0 6 0 2 0 7 8
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0'''

str_inp = '''0 0 0 0 0 0 0 0 0
0 0 0 7 8 9 0 2 3
0 8 0 0 2 3 4 5 6
0 0 4 0 6 5 0 9 7
0 6 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 6 5 3 1'''

inp = [[int(value) for value in row.split()] for row in str_inp.split('\n')]
playground = np.array(inp)
#playground = np.zeros(shape = (9, 9))

filled = playground.astype(bool)

row_marker = np.zeros(shape = (9, 10))

col_marker = np.zeros(shape = (9, 10))

sub_square_marker = np.zeros(shape = (3, 3, 10))

stop_flag = False

def reset_marker():
    
    global row_marker
    global col_marker
    global sub_square_marker
    
    row_marker = np.zeros(shape = (9, 10))
    col_marker = np.zeros(shape = (9, 10))
    sub_square_marker = np.zeros(shape = (3, 3, 10))

def solution():
    if (playground[0, 0] > 1):
        print('Okay')
    global count
    count += 1

def check(val, row, col) -> bool:
    '''Check if the value `val` can be placed in row `row` and column `col`. Return True if it can be, return False otherwise'''
    
    condition = row_marker[row, val] + col_marker[col, val] + sub_square_marker[row // 3, col // 3, val]
    return not condition

def mark(val, row, col, marking_value = 1) -> None:
    '''Mark the existence of value `val` in row `row` and column `col`'''
    row_marker[row, val] = marking_value
    col_marker[col, val] = marking_value
    sub_square_marker[row // 3, col // 3, val] = marking_value
    
def Try_next(row, col):
    if (row == 8) and (col == 8):
        solution()
        global stop_flag
        #stop_flag = True
    else:
        if (col == 8):
            Try(row = row+1, col=0)
        else:
            Try(row = row, col = col + 1)
            
    
def Try(row, col):
    '''Try to place value in row `row` and column `col`.'''
    
    if stop_flag:
        return
    
    if filled[row, col]:
        mark(val = int(playground[row, col]), row = row, col = col)
        Try_next(row = row, col = col)
    
    # Try values in range 1 to 9 (include ending point)
    for value in range(1, 10):
        
        if check(val = value, row = row, col = col):
            playground[row, col] = value
            mark(val = value, row = row, col = col)
            Try_next(row = row, col = col)
            mark(val = value, row = row, col = col, marking_value=0)
import time

start = time.time()
Try(0, 0)
print(f'Execution time: {time.time() - start}s')
print(f'Number of result found: {count}')


