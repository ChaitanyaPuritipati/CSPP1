'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 7-8-2018
'''
# Exercise: GCDIter
def gcd_iter(a_num, b_num):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a_num > b_num:
        min_val = b_num
    else:
        min_val = a_num
    while min_val >= 1:
        if a_num % min_val == 0 and b_num % min_val == 0:
            return min_val
        min_val = min_val-1
def main():
    '''
    Main function starts here
    '''
    input_num = input()
    input_num = input_num.split()
    print(gcd_iter(int(input_num[0]), int(input_num[1])))
if __name__ == "__main__":
    main()
