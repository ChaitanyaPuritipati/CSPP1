'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 10-08-2018
'''
def get_word_score(input_word, input_num):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    scrabble_letter_values = {\
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,\
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,\
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10\
    }
    counter_val = 0
    len_word = len(input_word)
    for i in input_word:
        if i in scrabble_letter_values:
            counter_val = counter_val + scrabble_letter_values[i]
    counter_val = counter_val*len_word    
    if  len_word == input_num:
        counter_val = counter_val + 50    
    return counter_val         

def main():
    '''
    Main function for the given problem
    '''
    input_data = input()
    input_data = input_data.split()
    print(get_word_score(input_data[0], int(input_data[1])))


if __name__ == "__main__":
    main()
