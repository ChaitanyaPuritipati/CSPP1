'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 9-8-2018
'''
#Exercise : how many
def how_many(a_dict1):
    '''
    #aDict: A dictionary, where all the values are lists.

    #returns: int, how many values are in the dictionary.
    '''
    values = list(a_dict1.values())
    return len(values)
def main():
    '''
    Main Function starts here
    '''
    input_num = int(input())
    a_dict = {}
    i_num = 0
    while i_num < input_num:
        s_str = input()
        l_list = s_str.split()
        if l_list[0][0] not in a_dict:
            a_dict[l_list[0][0]] = [l_list[1]]
        else:
            a_dict[l_list[0][0]].append(l_list[1])
        i_num = i_num+1
    print(how_many(a_dict))
if __name__ == "__main__":
    main()
