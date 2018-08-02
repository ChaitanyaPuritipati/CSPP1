'''
Author:Puritipati Chaitanya Prasad Reddy
Date: 2-8-2018
'''
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
def main():
    '''
    function is calculating the number of vowels
    '''
    s_1 = input()
    # the input string is in s
    # remove pass and start your code here
    end = len(s_1)
    vowelcount = 0
    for i in range(0, end):
        if (s_1[i] == 'a' \
            or s_1[i] == 'e' \
            or s_1[i] == 'i' \
            or s_1[i] == 'o' \
            or s_1[i] == 'u'):
            vowelcount = vowelcount + 1
    print(vowelcount)

if __name__ == "__main__":
    main()
