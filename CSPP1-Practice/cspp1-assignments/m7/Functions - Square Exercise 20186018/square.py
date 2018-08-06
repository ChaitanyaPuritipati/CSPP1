'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 6-8-2018
'''
# Exercise: square
# This function takes in one number and returns one number.
def square(x_num):
    '''
    x: int or float.
    '''
    return x_num**2
def main():
    '''
    main function starts here
    '''
    input_num = input()
    input_num = float(input_num)
    temp = str(input_num).split('.')
    if temp[1] == '0':
        print(square(int(float(str(input_num)))))
    else:
        print(square(input_num))

if __name__ == "__main__":
    main()
