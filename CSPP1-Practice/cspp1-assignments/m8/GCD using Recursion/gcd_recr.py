'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 7-8-2018
'''
# Exercise: GCDRecr
def gcd_recur(a_num, b_num):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b_num == 0:
        return a_num
    return gcd_recur(b_num, a_num % b_num)
def main():
    '''
    Main Function starts here
    '''
    input_num = input()
    input_num = input_num.split()
    print(gcd_recur(int(input_num[0]), int(input_num[1])))
if __name__ == "__main__":
    main()
