'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 7-8-2018
'''
# Exercise: Assignment-2
def sum_of_digits(n_num):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if n_num == 0:
        return 0
    return (n_num%10) + sum_of_digits(n_num//10)
def main():
    '''
    Main function starts here
    '''
    input_num = input()
    print(sum_of_digits(int(input_num)))
if __name__ == "__main__":
    main()
