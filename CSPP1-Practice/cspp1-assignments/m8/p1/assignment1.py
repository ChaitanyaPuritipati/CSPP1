'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 7-8-2018
'''
# Exercise: Assignment-1
def factorial_cal(n_num):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if n_num in (1, 0):
        return 1
    return n_num*factorial_cal(n_num-1)
def main():
    '''
    Main function starts here
    '''
    input_num = input()
    print(factorial_cal(int(input_num)))
if __name__ == "__main__":
    main()
