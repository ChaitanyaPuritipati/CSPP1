'''
Author:Puritipati Chaitanya Prasad Reddy
Date:2-8-2018
'''
#program to count no of bobs

def main():
    '''
    Function checking presence of substring
    '''
    s_1 = input()
    # the input string is in s
    # remove pass and start your code here
    end = len(s_1)
    ctr = "bob"
    stringcount = 0
    for i in range(0, end):
        if s_1[i:i+3] == ctr:
            stringcount = stringcount + 1
    print(stringcount)

if __name__ == "__main__":
    main()
