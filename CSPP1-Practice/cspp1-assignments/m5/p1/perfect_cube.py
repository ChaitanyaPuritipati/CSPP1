'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 4-8-2018
'''
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm
def main():
    '''
    Function is to check if the number is a perfect cube
    '''
    input_num = int(input())
    ans_num = 0
    step = 1
    while ans_num**3-abs(input_num) < 0:
        ans_num = ans_num+step
    if ans_num**3-abs(input_num) == 0:
        print(input_num, "is a perfect cube")
    else:
        print(input_num, "is not a perfect cube")
if __name__ == "__main__":
    main()
