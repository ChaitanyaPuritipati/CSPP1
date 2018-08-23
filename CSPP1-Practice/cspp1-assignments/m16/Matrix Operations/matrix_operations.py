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
    #print(rows)
    row_dict = {}
    count_ele = 0
    for row in range(rows):
        row_input = input().split()
        count_ele += len(row_input)
        row_dict[row] = row_input
    return (row_dict, count_ele)

def read_matrix(dimension_matrix1, matrix_1, dimension_matrix2, matrix_2, matrix_1_count, matrix_2_count):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    dimension_matrix1_ele = (int(dimension_matrix1[0]))*(int(dimension_matrix1[1]))
    dimension_matrix2_ele = (int(dimension_matrix2[0]))*(int(dimension_matrix2[1]))
    print(dimension_matrix1_ele, dimension_matrix2_ele)
    if matrix_1_count != dimension_matrix1_ele or matrix_2_count != dimension_matrix2_el:
        print("Error: Invalid input for the matrix") 
    return None    
def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    dimension_matrix1 = input().split(',')
    matrix_1 = Matrix_dict(dimension_matrix1)
    matrix_1_values = matrix_1[0]
    matrix_1_count = matrix_1[1]
    print(matrix_1, matrix_1_count)
    dimension_matrix2 = input().split(',')
    matrix_2 = Matrix_dict(dimension_matrix2)
    matrix_2_values = matrix_2[0]
    matrix_2_count = matrix_2[1]
    print(read_matrix(dimension_matrix1, matrix_1_values, dimension_matrix2, matrix_2_values, matrix_1_count, matrix_2_count))
if __name__ == '__main__':
    main()
