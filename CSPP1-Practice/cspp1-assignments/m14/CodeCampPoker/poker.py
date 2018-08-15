'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 14-08-2018
'''
#Write a program to evaluate poker hands and determine the winner
#Read about poker hands here.
#https://en.wikipedia.org/wiki/List_of_poker_hands
FACE_VALUES = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7,\
'8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    test_string = []
    value_list = list(FACE_VALUES.values())
    keys_list = list(FACE_VALUES.keys())
    i = 0
    while i < (len(hand)):
        test_string.append(FACE_VALUES[hand[i][0]])
        i = i + 1
    test_string.sort()
    if test_string[0] == 2 and test_string[4] == 14:
        temp = test_string[0]
        test_string[0] = test_string[4]
        test_string[4] = temp
        test_string = ''.join(str(x) for x in test_string)
    else:
        j = 0
        for k in test_string:
            test_string[j] = keys_list[value_list.index(k)]
            j = j + 1
        test_string = ''.join(str(x) for x in test_string)
    if test_string in "A23456789TJQKA":
        return True
    return False
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush    []
        Write the code for it and return True if it is a flush else return False
    '''
    test_string_flush = ""
    l_num = 0
    while l_num < (len(hand)):
        test_string_flush = test_string_flush + hand[l_num][1]
        l_num = l_num + 1
    if test_string_flush in "SSSSS":
        return True
    if test_string_flush in "HHHHH":
        return True
    if test_string_flush in "DDDDD":
        return True
    if test_string_flush in "CCCCC":
        return True
    return False
def four_of_kind(hand):
    z = 0
    test_kind = set()
    while z < len(hand):
        test_kind.update(hand[z][0])
        z = z + 1
    #print(test_kind)
    #print(len(test_kind))   
    if len(test_kind) == 2:
        count_list =[]
        for i in test_kind:
            count_list.append(hand.count(i))
        print(count_list)    
        if 4 in count_list:
            return True
    return False
def full_house(hand):
    z = 0
    test_kind = set()
    while z < len(hand):
        test_kind.update(hand[z][0])
        z = z + 1
    print(test_kind)    
    #print(len(test_kind))
    if len(test_kind) == 2:
        count_list =[]
        for i in test_kind:
            count_list.append(hand.count(str(i)))
        print(count_list)
        if 3 in count_list:
            return True
    return False     
def three_of_kind(hand):
    y = 0
    test_kind_new = set()
    while y < len(hand):
        test_kind_new.update(hand[y][0])
        y = y + 1
    #print(test_kind_new) 
    #print(len(test_kind_new))   
    if len(test_kind_new) == 3:
        count_list =[]
        for i in test_kind_new:
            count_list.append(hand.count(i))
        print(count_list)
        if 3 in count_list:
            return True
    return False  
def two_pair(hand):
    y = 0
    test_kind_new = set()
    while y < len(hand):
        test_kind_new.update(hand[y][0])
        y = y + 1
    #print(test_kind_new)
    #print(len(test_kind_new)) 
    if len(test_kind_new) == 3:
        count_list =[]
        for i in test_kind_new:
            count_list.append(hand.count(i))
        print(count_list)
        if  count_list.count(2) == 2:
            return True
    return False     
def one_pair(hand):
    z = 0
    test_kind = set()
    while z < len(hand):
        test_kind.update(hand[z][0])
        z = z + 1
    #print(test_kind)
    #print(len(test_kind))
    if len(test_kind) == 4:
        return True
    return False
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_straight(hand) and is_flush(hand):
        print("test9")
        return 9
    if four_of_kind(hand):
        print("test8")
        return 8
    if full_house(hand):
        print("test7")
        return 7
    if is_flush(hand):
        print("test6")
        return 6
    if is_straight(hand):
        print("test5")
        return 5
    if three_of_kind(hand):
        print("test4")
        return 4
    if two_pair(hand):
        print("test3")
        return 3
    if one_pair(hand):
        print("test2")
        return 2    
    print("test1")         
    return 1
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
