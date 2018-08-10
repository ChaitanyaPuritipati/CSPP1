'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 10-8-2018
'''
#Exercise: Assignment-4
def calculate_handlen(test_hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    counter_val = 0
    for i_char in test_hand:
        counter_val = counter_val + test_hand[i_char]
    return counter_val
def main():
    '''
    Main function starts here
    '''
    n_num = input()
    a_dict={}
    i_num = 0
    while i_num < (int(n_num)):
        input_data = input()
        l_list = input_data.split()
        a_dict[l_list[0]]=int(l_list[1])
        i_num = i_num + 1
    print(calculate_handlen(a_dict))
if __name__ == "__main__":
    main()