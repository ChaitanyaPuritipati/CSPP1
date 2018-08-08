'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 8-8-2018
'''
#Exercise : Function and Objects Exercise-3
#Module_9
def square_func(temp_num):
    '''
    This function returns square of the number
    '''
    return temp_num**2
def apply_to_each(arb_list, f_func):
    '''
    This function is to return the output list
    '''
    list_2 = []
    for k in arb_list:
        list_2.append(f_func(k))
    return list_2
def main():
    '''
    Main function starts here
    '''
    input_data = input()
    input_data = input_data.split()
    list_1 = []
    for j in input_data:
        list_1.append(int(j))
    print(apply_to_each(list_1, square_func))
if __name__ == "__main__":
    main()
