'''
Author: P.Chaitanya Prasad Reddy
Roll no: 20186018
Date: 25-08-2018
CSPP1 EXAM WEEK 4
-----------------------------------------------------------------------------------------
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
def frequency_graph(dictionary):
    '''
    Frequency graph function starts here
    '''
    dict_keys = list(dictionary.keys())
    dict_values = list(dictionary.values())
    dict_test_keys = dict_keys[:]
    dict_test_keys.sort()
    for every_val in dict_test_keys:
        print(every_val + " " + "-" + " "+ str(dict_values[dict_keys.index(every_val)]*'#'))
def main():
    '''
    Main function starts here
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
