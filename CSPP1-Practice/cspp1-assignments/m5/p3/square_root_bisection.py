'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 4-8-2018
'''
# Write a python program to find the square root of the given number
# using bisection method
def main():
    '''
    function is to find the sqaure root of a number using bisection method
    '''
    input_num = int(input())
    epsilon = 0.01
    initial_value = 0.0
    end_value = input_num
    guess_val = (initial_value + end_value)/2.0
    while abs(guess_val**2-input_num) >= epsilon:
        if guess_val**2 > input_num:
            end_value = guess_val
        else:
            initial_value = guess_val
        guess_val = (initial_value + end_value)/2.0
    if guess_val > input_num:
        print("Failed")
    else:
        print(guess_val)
if __name__ == "__main__":
    main()
