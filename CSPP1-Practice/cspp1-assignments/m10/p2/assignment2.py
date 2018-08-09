'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 9-8-2018
'''
'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
def get_guessed_word(secret_word, letters_guessed, list_temp):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    k = 0
    ln_secretword = len(secret_word)
    while k < len(letters_guessed):
        if letters_guessed[k] in secret_word:
            for j in range(ln_secretword):
                if letters_guessed[k] == secret_word[j]:
                    list_temp[j] = str(letters_guessed[k])
        k = k + 1
    output_string = ''.join(str(c) for c in list_temp)
    return output_string
def get_available_letters(letters_guessed, str_1):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str_1 = list(str_1)
    i = 0
    temp_letters = letters_guessed[:]
    while i < len(letters_guessed):
        if letters_guessed[i] in temp_letters[0:i]:
            temp_letters = letters_guessed[:]
        else:
            str_1.remove(letters_guessed[i])
        i = i+1
    str_1 = ''.join(str(e) for e in str_1)
    return str_1
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    i = 0
    list_temp = []
    ln_secretword = len(secretWord)
    list_guesses = []
    str_1 = "abcdefghijklmnopqrstuvwxyz"
    while i < ln_secretword:
        list_temp.append('_')
        i = i+1
    while guesses > 0:
        print("Available Letters: "+str_1)
        n = input("Please guess a letter: ")
        if n not in list_guesses:
            list_guesses.append(n)
            if n in secretWord:
                print("Good guess: "+ str(get_guessed_word(secretWord, n, list_temp)))
                str_1 = get_available_letters(n, str_1)
            else:
                guesses = guesses - 1
                str_1 = get_available_letters(n, str_1)
                print("Oops! That letter is not in my word: "+(''.join(str(c) for c in list_temp)))
            if (''.join(str(c) for c in list_temp)) == secretWord:
                print("--------------------------------------")
                return "Congratulations, you won!"
            else:
                print("You have "+ str(guesses) +" guesses left")
                print("--------------------------------------")
        else:
            print("Oops! You've already guessed that letter: "+ str(get_guessed_word(secretWord, n, list_temp)))
            print("You have "+ str(guesses) +" guesses left")
            print("--------------------------------------")
    return "Sorry, you ran out of guesses. The word was "+ str(secretWord)

def main():
    '''
    Main function for the given program
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    word_count = len(secretWord)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+ str(word_count) +" letters long.")
    print("--------------------------------------")
    #secretWord = "apple"
    print(hangman(secretWord))


if __name__ == "__main__":
    main()
