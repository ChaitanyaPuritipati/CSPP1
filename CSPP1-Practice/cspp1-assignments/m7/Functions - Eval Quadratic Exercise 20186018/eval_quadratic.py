'''
Author: Puritipati Chaitanya prasad Reddy
Date: 6-8-2018
'''
#To find Quadratic function
def eval_quadratic(a_num, b_num, c_num, x_num):
    '''
    Function is to evaluate quadratic function
    '''
    sum_num = (a_num*(x_num**2)) + (b_num*x_num) + c_num
    return sum_num
def main():
    '''
    Main Function starts here
    '''
    input_num = input()
    input_num = input_num.split(' ')
    input_num = list(map(float, input_num))
    # print(data)
    for x_num in range(len(input_num)):
        temp_num = str(input_num[x_num]).split('.')
        if temp_num[1] == '0':
            input_num[x_num] = int(float(str(input_num[x_num])))
        else:
            input_num[x_num] = input_num[x_num]
    print(eval_quadratic(input_num[0], input_num[1], input_num[2], input_num[3]))

if __name__ == "__main__":
    main()
