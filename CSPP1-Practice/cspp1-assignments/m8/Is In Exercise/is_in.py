'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 7-8-2018
'''
# Exercise: Is In
def is_in(char, input_str):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    global low_val
    global high_val 
    global middle_val
    middle_val = (low_val + high_val)//2
    if low_val == high_val:
        return False
    if input_str[middle_val] == char:
        return True
    if input_str[middle_val] > char:
        high_val = middle_val-1
        return is_in(char, input_str)
    if input_str[middle_val] < char:
        low_val = middle_val+1
        return is_in(char, input_str) 
def main():
    '''
    Main Function starts here
    '''
    data_1 = input()
    data_2 = input()
    if data_2 == "":
        return print("False")
    else:
        string_sort = sorted(data_2)
        string_sort = ''.join(string_sort)
        global low_val
        global high_val 
        global middle_val
        low_val = 0
        high_val = len(data_2)
        print(is_in(data_1, string_sort))
if __name__== "__main__":
    main()
