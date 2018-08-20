'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 20-08-2018
Module 13
-----------------------------------------------------------------------------------------
'''
#define the simple_divide function here
def simple_divide(item, denom):
    # start a try-except block
    try:
        return item/denom
    except ZeroDivisionError:
        return 0    
def fancy_divide(list_of_numbers, index):
    '''
    function to return output list
    '''
    output_list = []
    for everynum in list_of_numbers:
        output_list.append(simple_divide(everynum, list_of_numbers[index]))
    return output_list
def main():
    '''
    Main function starts here
    '''
    data = input()
    l=data.split()
    l1=[]
    for j in l:
        l1.append(float(j))
    s=input()
    index=int(s)
    print(fancy_divide(l1,index))
    

if __name__== "__main__":
    main()
