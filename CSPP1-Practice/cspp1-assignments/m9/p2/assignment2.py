'''
Exercise: Assignment-2
Next, implement the function getGuessedWord that takes in two parameters
a string, secret_word, and a list of letters, letters_guessed. This function
returns a string that is comprised of letters and underscores, based on what
letters in letters_guessed are in secret_word. This shouldn't be too different from isWordGuessed!
'''
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
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
    Main function for current assignment
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()
