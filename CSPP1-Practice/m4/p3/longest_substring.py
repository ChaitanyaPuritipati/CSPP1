'''
Author:Puritipati Chaitanya Prasad Reddy
Date: 2-8-2018
'''
#Assume s is a string of lower case characters.
#CSPP1_M4_A3
def main():
    '''
    function to check the sequence of alphabets
    '''
    s_1 = input()
    # the input string is in s
    # remove pass and start your code here
    counter_loop = 0
    max_value = 0
    end_value = 0
    ln_1 = len(s_1)
    for i in range(ln_1-1):
        if ord(s_1[i]) <= ord(s_1[i+1]):
            counter_loop = counter_loop + 1
        else:
            counter_loop = 0
        if max_value < counter_loop:
            max_value = counter_loop
            end_value = i + 1
    k_1 = s_1[end_value - max_value : end_value+1]
    print(k_1)
if __name__ == "__main__":
    main()
