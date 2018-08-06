'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 6-8-2018
'''
#Odd number exercise
def odd(x_num):
    '''
    x: int or float.
    returns: True if x is odd, False otherwise
    '''
    return x_num%2 == 0
def main():
    '''
    Main Function is to check the odd number
    '''
    input_num = input()
    print(odd(int(input_num)))

if __name__ == "__main__":
    main()
