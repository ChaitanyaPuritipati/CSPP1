'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 5-8-2018
'''
# Write a python program to find the square root of the given number
#Newton-Raphson Method
def main():
    '''
    function is to calculate square root of a number using newton raphson method
    '''
    input_num = int(input())
    epsilon = 0.01
    guess_val = input_num/2.0
    while abs(guess_val**2 - input_num) >= epsilon:
        guess_val = guess_val - ((guess_val**2 - input_num)/(2*guess_val))
    print(guess_val)
if __name__ == "__main__":
    main()
