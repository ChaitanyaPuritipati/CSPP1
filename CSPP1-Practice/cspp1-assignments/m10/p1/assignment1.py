'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 9-8-2018
'''
#Exercise A1
def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str_1 = "abcdefghijklmnopqrstuvwxyz"
    str_1 = list(str_1)
    temp_letters = letters_guessed[:]
    while i < len(letters_guessed):
        if letters_guessed[i] in temp_letters[0:i]:
            temp_letters = letters_guessed[:]
        else:
            str_1.remove(letters_guessed[i])
        i = i+1    
    str_1 = ''.join(str(e) for e in str_1)
    return str_1
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
