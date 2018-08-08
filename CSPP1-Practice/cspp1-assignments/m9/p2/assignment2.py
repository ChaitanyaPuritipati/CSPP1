'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 8-8-2018
'''
#Exercise Assignment 2
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    ln_secretword = len(secret_word)
    i = 0
    list_temp = []
    while i < ln_secretword:
        list_temp.append('_')
        i = i+1
    k = 0
    while k < len(letters_guessed):
        if letters_guessed[k] in secret_word:
            for j in range(ln_secretword):
                if letters_guessed[k] == secret_word[j]:
                    list_temp[j] = str(letters_guessed[k])
        k = k + 1
    output_string = ''.join(str(c) for c in list_temp)
    return output_string
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
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()
