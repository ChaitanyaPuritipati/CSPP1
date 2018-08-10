'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 10-8-2018
'''
#Exercise: Integer Division Exercise
#Modify the code for integer_division so that this error does not occur.
def integer_division(x_num, a_num):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count_val = 0
    while x_num >= a_num:
        count_val += 1
        x_num = x_num - a_num
    return count_val

def main():
    '''
    Main Function starts here
    '''
    input_data = input()
    input_data = input_data.split()
    print(integer_division(int(input_data[0]), int(input_data[1])))


if __name__ == "__main__":
    main()
