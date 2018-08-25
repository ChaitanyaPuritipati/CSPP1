'''
Author: P.Chaitanya Prasad Reddy
Roll no: 20186018
Date: 25-08-2018
CSPP1 EXAM WEEK 4
----------------------------------------------------------------------------------------------
Write a python program to read multiple lines of text input and store the input into a string.
'''
def main():
    '''
    Main function starts here
    '''
    lines_num = int(input())
    for every_line in range(lines_num):
        print(input())
        every_line += 1

if __name__ == '__main__':
    main()
