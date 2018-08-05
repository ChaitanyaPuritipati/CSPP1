'''
Author:Puritipati Chaitanya Prasad Reddy
Date:4-8-2018
'''
#Using approximation method
def main():
    '''
    Function is to calculate the sqaure root using approximation method
    '''
    input_num = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    step = 0.1
    # your code starts here
    guess_num = 0.0
    while (abs(guess_num**2-input_num) >= epsilon) and (guess_num <= input_num):
        guess_num = guess_num + step
    if abs(guess_num**2-input_num) < epsilon:
        print(guess_num)
    else:
        print("failed")
if __name__ == "__main__":
    main()
