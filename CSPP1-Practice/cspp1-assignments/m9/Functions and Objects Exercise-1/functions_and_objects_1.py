'''
Author: Puritipaati Chaitanya Prasad Reddy
Date: 8-8-2018
'''
#Exercise : Function and Objects Exercise-1
#Module_9
def apply_to_each(l_list, f_func):
    '''
    This function is used to find absolute values of the elements
    '''
    k = 0
    output_list_ln = len(l_list)
    while k < output_list_ln:
        if l_list[k] < 0:
            l_list[k] = f_func(l_list[k])
        k = k + 1
    return l_list
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
    print(apply_to_each(list_1, abs))
if __name__ == "__main__":
    main()
