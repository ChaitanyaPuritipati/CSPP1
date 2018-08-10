'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 10-8-2018
'''
#Assignment-3
#Module_11 
def is_valid_word(test_word, test_hand, test_wordlist):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    count_word = 0
    for i_char in test_word:
        if i_char in test_hand:
            count_word = count_word + 1
    if count_word != len(test_word):
        return False
    ln_wordlist = len(test_wordlist)
    for i_num  in range(ln_wordlist):
        if test_word in test_wordlist[i_num]:
            return True
    return False
def main():
    '''
    Main function starts here
    '''
    input_word = input()
    n_num = int(input())
    a_dict = {}
    for i in range(n_num):
        input_data = input()
        l_list = input_data.split()
        a_dict[l_list[0]]=int(l_list[1])
    l_newlist=input().split()
    print(is_valid_word(input_word, a_dict, l_newlist))
if __name__== "__main__":
    main()
