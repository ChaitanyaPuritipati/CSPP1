'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
'''

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str_1 = "abcdefghijklmnopqrstuvwxyz"
    str_1 = list(str_1)
    temp_letters = letters_guessed[:]
    for i in letters_guessed:
        if i in temp_letters[0:i]:
            temp_letters = letters_guessed[:]
        else:   
            str_1.remove(i)
    str_1 = ''.join(str_1(e) for e in range(len(str_1)))        
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
