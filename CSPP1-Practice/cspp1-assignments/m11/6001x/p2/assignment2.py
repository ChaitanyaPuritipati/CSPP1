'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 10-8-2018
'''
#Exercise: Assignment-2
#module_11
def update_hand(hand_dict, test_word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    test_word = list(test_word)
    for i_test in test_word:
        if i_test in hand_dict:
            hand_dict[i_test] = hand_dict[i_test]-1
    return hand_dict
def main():
    '''
    Main function starts here
    '''
    n_data = input()
    a_dict = {}
    for i in range(int(n_data)):
        input_data = input()
        l_data = input_data.split()
        a_dict[l_data[0]] = int(l_data[1])
    data_1 = input()
    print(update_hand(a_dict, data_1))
if __name__ == "__main__":
    main()
