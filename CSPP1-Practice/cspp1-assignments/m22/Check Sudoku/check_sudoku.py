'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def check_grid(sudoku):
    new_rows = []
    for every_row in sudoku:
        i = 0
        while i < (len(sudoku[0])-2):
            print(sudoku[i:i+3])
            new_rows.append([sudoku[i:i+3]])
            i = i+3
    #print(new_rows)
# def check_col(sudoku):
#     for every_row in range(len(sudoku)):
#         col_set = set()
#         for every_col in range(len(sudoku[0])):
#             col_set.add(sudoku[every_col][every_row])
#         if len(col_set) != len(sudoku):
#             return False
#     return True            
# def check_row(sudoku):
#     for every_row in sudoku:
#         if len(set(every_row)) != len(sudoku):
#             return False
#     return True
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    check_grid(sudoku)

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()