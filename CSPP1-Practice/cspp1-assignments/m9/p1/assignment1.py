'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 8-8-2018
'''
#Exercise Assignment 1
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if len(secret_word) is 0:
        return "True"
    length_lettersguessed = len(letters_guessed)
    length_word = len(secret_word)
    sum_count = 0
    temp = letters_guessed[:]
    for i in range(length_lettersguessed):
        if i in temp[0:i]:
            temp = letters_guessed[:]
        else:
            if letters_guessed[i] in secret_word:
                sum_count = sum_count + secret_word.count(letters_guessed[i])
            if sum_count == length_word:
                return "True"
    if sum_count < length_word:
        return "False"
    return "True"
def main():
    '''
    Main function starts here
    '''
    user_input = input()
    if user_input:
        input_data = user_input.split()
        secret_word = input_data[0]
    else:
        input_data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(input_data)):
        list1.append(input_data[j][0])
    print(is_word_guessed(secret_word, list1))
if __name__ == "__main__":
    main()
