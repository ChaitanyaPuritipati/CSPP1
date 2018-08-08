'''
Exercise: Assignment-1
First, implement the function isWordGuessed that takes in two parameters -
a string, secret_word, and a list of letters, letters_guessed. This function
returns a boolean - True if secret_word has been guessed (ie, all the letters of
secret_word are in letters_guessed) and False otherwise.
'''


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

def main():
    '''
    Main function for the program
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
    print(is_word_guessed(secret_word, list1))
if __name__ == "__main__":
    main()
