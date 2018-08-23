def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    pass
def Matrix_dict(dimension_matrix):
    rows = int(dimension_matrix[0])
    row_dict = {}
    for row in range(rows):
        row_dict[row] = input()    
    return row_dict    

def read_matrix(dimension_matrix1, matrix_1, dimension_matrix2, matrix_2):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    if dimension_matrix1[0] != len(matrix_1.keys()) or dimension_matrix1[1] != len(matrix_1.values()):
        print(Error: Invalid input for the matrix)
    if dimension_matrix2[0] != len(matrix_2.keys()) or dimension_matrix2[1] != len(matrix_2.values()):
        print(Error: Invalid input for the matrix)    
    return None    
def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    dimension_matrix1 = input().split(',')
    matrix_1 = Matrix_dict(dimension_matrix1)
    dimension_matrix2 = input().split(',')
    matrix_2 = Matrix_dict(dimension_matrix2)
    print(read_matrix(dimension_matrix1, matrix_1, dimension_matrix2, matrix_2))
if __name__ == '__main__':
    main()
