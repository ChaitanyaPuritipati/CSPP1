'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 8-8-2018
'''
#Exercise : Function and Objects Exercise-2
#module_9
def inc_one(temp_num):
    '''
    This function is used to increment the numbers
    '''
    return temp_num+1
def apply_to_each(temp_list, f_func):
    '''
    This function is to return the output incremented list
    '''
    l_num = 0
    ln_list = len(temp_list)
    while l_num < ln_list:
        temp_list[l_num] = f_func(temp_list[l_num])
        l_num = l_num+1
    return temp_list
def main():
    '''
    Main function starts here
    '''
    input_data = input()
    input_data = input_data.split()
    list_1 = []
    list_1_ln = len(input_data)
    j = 0
    while j < list_1_ln:
        list_1.append(int(input_data[j]))
        j = j+1
    print(apply_to_each(list_1, inc_one))

if __name__ == "__main__":
    main()
