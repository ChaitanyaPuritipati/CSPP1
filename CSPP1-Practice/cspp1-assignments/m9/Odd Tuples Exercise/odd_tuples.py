'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 8-8-2018
'''
#Exercise : Odd Tuples
#Module_9
def odd_tuples(ar_tup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    output_tuple = ()
    return output_tuple + ar_tup[::2]
def main():
    '''
    Main Function starts here
    '''
    input_data = input()
    input_data = input_data.split()
    input_tup = ()
    j = 0
    while j < len(input_data):
        input_tup += (int(input_data[j]),)
        j = j+1
    print(odd_tuples(input_tup))
if __name__ == "__main__":
    main()
