'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 14-08-2018
'''
#Write a program to evaluate poker hands and determine the winner
#Read about poker hands here.
#https://en.wikipedia.org/wiki/List_of_poker_hands
FACE_VALUES = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7,\
'8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
def is_check_other(hands, test_index):
    list_first_values = []
    for j in test_index:
        first_values = []
        for k in hands[j]:
            first_values.append(FACE_VALUES[k[0]])
        first_values.sort(reverse=True)
        list_first_values.append(first_values)
    o = 0
    i = 0
    while o < len(list_first_values):
        list_hand_values = []
        for j in list_first_values:
            list_hand_values.append(j[i])    
        max_val = max(list_hand_values)
        max_count = list_hand_values.count(max_val)
        if max_count == 1:
            v = list_hand_values.index(max_val)
            return hands[v]
        i = i + 1
        o = o + 1

    return hands[0]



def is_check_one_pair(hands, test_index):
    list_check_four = []
    for j in test_index:
        first_values = {}
        for k in hands[j]:
            if k[0] in first_values:
                first_values[k[0]] = first_values[k[0]] + 1
            else:
                first_values[k[0]] = 1
        values_list_dict = list(first_values.values())
        keys_list_dict = list(first_values.keys())
        list_test = []
        #var_max = values_list_dict.index(max(values_list_dict))
        #key_max = keys_list_dict[values_list_dict.index(max(values_list_dict))]
        #print(key_max)
        keys_list_dict.remove(keys_list_dict[values_list_dict.index(max(values_list_dict))])
        for l in keys_list_dict:
            list_test.append(FACE_VALUES[l])
        list_test.sort(reverse=True)
        list_test.insert(0, keys_list_dict[values_list_dict.index(max(values_list_dict))])
        list_check_four.append(list_test)
    i = 0
    o = 0
    while o < len(list_check_four):
        list_hand_values = []
        for j in list_check_four:
            list_hand_values.append(j[i])
        max_val = max(list_hand_values)
        max_count = list_hand_values.count(max_val)
        if list_hand_values.count(max(list_hand_values)) == 1:
            list_hand_values.index(max(list_hand_values))
            return hands[list_hand_values.index(max(list_hand_values))]
        i = i + 1
        o = o + 1
    return hands[0]
def is_check_four_kind(hands, test_index):
    list_check_four = []
    for j in test_index:
        first_values = {}
        for k in hands[j]:
            if k[0] in first_values:
                first_values[k[0]] = first_values[k[0]] + 1
            else:
                first_values[k[0]] = 1
        values_list_dict = list(first_values.values())
        keys_list_dict = list(first_values.keys())
        list_test = []
        var_max = values_list_dict.index(max(values_list_dict))
        key_max = int(keys_list_dict[var_max])
        keys_list_dict.remove(keys_list_dict[var_max])
        for l in keys_list_dict:
            list_test.append(FACE_VALUES[l])
        list_test.sort(reverse=True)
        list_test.insert(0, key_max)
        list_check_four.append(list_test)
    i = 0
    o = 0
    while o < len(list_check_four):
        list_hand_values = []
        for j in list_check_four:
            list_hand_values.append(j[i])
        #max_val = max(list_hand_values)
        #max_count = list_hand_values.count(max_val)
        if list_hand_values.count(max(list_hand_values)) == 1:
            #v = list_hand_values.index(max_val)
            return hands[list_hand_values.index(max_val)]
        i = i + 1
        o = o + 1
    return hands[0]
def counter_list_func(hand, test_kind):
    '''
    Function to return the frequency of elements in a list
    '''
    count_list = []
    for i in test_kind:
        counter = 0
        for j in hand:
            if i is j[0]:
                counter = counter + 1
        count_list.append(counter)
    return count_list
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
def is_four_of_kind(hand):
    '''
    Function to check four of kind
    '''
    z_num = 0
    test_kind = set()
    while z_num < len(hand):
        test_kind.update(hand[z_num][0])
        z_num = z_num + 1
    if len(test_kind) == 2:
        count_list = counter_list_func(hand, test_kind)
        if 4 in count_list:
            return True
    return False
def is_full_house(hand):
    '''
    Function to check for full house
    '''
    z_num = 0
    test_kind = set()
    while z_num < len(hand):
        test_kind.update(hand[z_num][0])
        z_num = z_num + 1
    if len(test_kind) == 2:
        count_list = counter_list_func(hand, test_kind)
        if 3 in count_list:
            return True
    return False
def is_three_of_kind(hand):
    '''
    Function to check three of kind
    '''
    y_num = 0
    test_kind_new = set()
    while y_num < len(hand):
        test_kind_new.update(hand[y_num][0])
        y_num = y_num + 1
    if len(test_kind_new) == 3:
        count_list = counter_list_func(hand, test_kind_new)
        if 3 in count_list:
            return True
    return False
def is_two_pair(hand):
    '''
    Function to check two pair
    '''
    y_num = 0
    test_kind_new = set()
    while y_num < len(hand):
        test_kind_new.update(hand[y_num][0])
        y_num = y_num + 1
    if len(test_kind_new) == 3:
        count_list = counter_list_func(hand, test_kind_new)
        if  count_list.count(2) == 2:
            return True
    return False
def is_one_pair(hand):
    '''
    Function to check for one pair
    '''
    z_num = 0
    test_kind = set()
    while z_num < len(hand):
        test_kind.update(hand[z_num][0])
        z_num = z_num + 1
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
        return 9
    if is_four_of_kind(hand):
        return 8
    if is_full_house(hand):
        return 7
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if is_three_of_kind(hand):
        return 4
    if is_two_pair(hand):
        return 3
    if is_one_pair(hand):
        return 2
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
    test_list = []
    test_index = []
    for j in hands:
        test_list.append(hand_rank(j))
    for j in range(len(test_list)):
        if max(test_list) is test_list[j]:
            test_index.append(j)
    if len(test_index) > 1:
        if max(test_list) == 8:
            return is_check_four_kind(hands, test_index)
        if max(test_list) == 1:
            return is_check_other(hands, test_index)    
        if max(test_list) == 2:
            return is_check_one_pair(hands, test_index)
        if max(test_list) == 2:
            return is_check_other(hands, test_index)    
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
