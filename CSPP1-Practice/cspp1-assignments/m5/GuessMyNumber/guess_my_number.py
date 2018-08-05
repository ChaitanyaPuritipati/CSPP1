'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 4-8-2018
'''
#Guess My Number Exercise
def main():
    '''
    Function is to guess the secret number
    '''
    min_val = 0
    max_val = 100
    avg_val = (min_val + max_val)//2
    input_char = ""
    while input_char != 'c':
        print("Is your secret number "+str(avg_val)+"?")
        input_char = input("Enter either 'h' or 'l or 'c'")
        if input_char in 'hlc':
            if input_char == 'h':
                max_val = avg_val
            if input_char == 'l':
                min_val = avg_val
            avg_val = (min_val + max_val)//2
        else:
            input_char = input("Enter a valid input among 'h' or 'l' or 'c'")
    print("Secret Number is:", avg_val)

if __name__ == "__main__":
    main()
