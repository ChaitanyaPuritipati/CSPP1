'''
Author: Puritipati Chaitanya Prasad Reddy
date: 4-8-2018
File: 20186018_CSPP1_week1_exam_fizz_buzz.py
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num = int(input())
    for i in range(num+1):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        if i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz")
            print("Buzz")
if __name__ == "__main__":
    main()
