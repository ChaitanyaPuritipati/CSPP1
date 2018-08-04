'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 4-8-2018
File: 20186018_CSPP1_week1_exam_digit_product.py
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    temp_var = int_input
    if temp_var == 0:
        dig_product = 0
    else:
        dig_product = 1
        while temp_var != 0:
            dig_remainder = temp_var % 10
            dig_product = dig_product * dig_remainder
            temp_var = temp_var//10
    print(dig_product)
if __name__ == "__main__":
    main()
