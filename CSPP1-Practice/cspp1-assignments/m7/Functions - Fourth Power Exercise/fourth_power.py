'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 6-8-2018
'''
def square_num(x_num):
    '''
    x: int or float.
    '''
    return x_num**2
def fourth_power_num(x_num):
    '''
    x: int or float.
    '''
    return square_num(x_num)**2
def main():
    '''
    Main Function starts here
    '''
    input_num = input()
    input_num = float(input_num)
    temp_num = str(input_num).split('.')
    if temp_num[1] == '0':
        print(fourth_power_num(int(float(str(input_num)))))
    else:
        print(fourth_power_num(input_num))

if __name__ == "__main__":
    main()
