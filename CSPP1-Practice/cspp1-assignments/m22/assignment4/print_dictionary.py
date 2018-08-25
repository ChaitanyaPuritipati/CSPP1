'''
Author: P.Chaitanya Prasad Reddy
Roll no: 20186018
Date: 25-08-2018
CSPP1 EXAM WEEK 4
-----------------------------------------------------------------------------------------
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''
    Function to print dictionary in the required format
    '''
    dict_keys = list(dictionary.keys())
    dict_values = list(dictionary.values())
    dict_test_keys = dict_keys[:]
    dict_test_keys.sort()
    for every_val in dict_test_keys:
        print(every_val + " " + "-" + " "+ str(dict_values[dict_keys.index(every_val)]))

def main():
    '''
    Main function starts here
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
