'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 7-8-2018
'''
# Exercise: PowerRecr
def recur_power(base_num, exp_num):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp_num == 0:
        return 1
    return base_num*recur_power(base_num, exp_num-1)
def main():
    '''
    Main function starts here
    '''
    input_num = input()
    input_num = input_num.split()
    print(recur_power(float(input_num[0]), int(input_num[1])))

if __name__ == "__main__":
    main()
