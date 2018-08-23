from operator import add
def type_conv(m1):
    m1_val = list(m1.values())
    for ele in range(len(m1_val)):
        m1_val[ele] = list(map(int, m1_val[ele]))
    return m1_val    
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if int(dimension_matrix1[1]) != int(dimension_matrix2[0]):
        print("Error: Matrix shapes invalid for mult")
        return None

def add_matrix(m1, m2,dimension_matrix1, dimension_matrix2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if int(dimension_matrix1[0]) != int(dimension_matrix1[0]) or int(dimension_matrix1[1]) != int(dimension_matrix2[1]):
        print("Error: Matrix shapes invalid for addition")
        return None
    m1_val = type_conv(m1)
    m2_val = type_conv(m2)
    added_matrix = []
    for ele in range(len(m1_val)):
        added_matrix.append(list(map(add, m1_val[ele], m2_val[ele])))
    return added_matrix    
def Matrix_dict(dimension_matrix):
    rows = int(dimension_matrix[0])
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
    if matrix_1_count != dimension_matrix1_ele or matrix_2_count != dimension_matrix2_ele:
        print("Error: Invalid input for the matrix")
        return None
    print(add_matrix(matrix_1, matrix_2, dimension_matrix1, dimension_matrix2))
     
def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    dimension_matrix1 = input().split(',')
    matrix_1 = Matrix_dict(dimension_matrix1)
    matrix_1_values = matrix_1[0]
    matrix_1_count = matrix_1[1]
    dimension_matrix2 = input().split(',')
    matrix_2 = Matrix_dict(dimension_matrix2)
    matrix_2_values = matrix_2[0]
    matrix_2_count = matrix_2[1]
    read_matrix(dimension_matrix1, matrix_1_values, dimension_matrix2, matrix_2_values, matrix_1_count, matrix_2_count))
if __name__ == '__main__':
    main()
