'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 9-8-2018
'''
#Exercise : Biggest Exercise
def biggest(a_func):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    values_1 = list(a_func.values())
    max_value = len(values_1[0])
    keys_1 = list(a_func.keys())
    max_key = keys_1[0]
    for i in a_func:
        if len(a_func[i]) > max_value:
            max_value = len(a_func[i])
            max_key = i
    return max_key

def main():
    '''
    Main function starts here
    '''
    n_num = int(input())
    a_dict = {}
    i = 0
    while i < n_num:
        s_str = input()
        l_list = s_str.split()
        if l_list[0][0] not in a_dict:
            a_dict[l_list[0][0]] = [l_list[1]]
        else:
            a_dict[l_list[0][0]].append(l_list[1])
        i = i+1
    print(biggest(a_dict))


if __name__ == "__main__":
    main()
