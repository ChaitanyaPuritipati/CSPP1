'''
Author: P.Chaitanya Prasad Reddy
Roll no: 20186018
Date: 25-08-2018
CSPP1 EXAM WEEK 4
-----------------------------------------------------------------------------------------
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    '''
    Function to clean a string
    '''
    output_str = ""
    for every_char in string:
        if every_char not in '!@#$%^&*()., ':
            output_str += every_char
    return output_str
def main():
    '''
    Main function starts here
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
