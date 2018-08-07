'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 7-8-2018
'''
# Exercise: PowerIter
def iter_power(base_num, exp_num):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp_num == 0:
        return 1
    power_num = 1
    while exp_num > 0:
        power_num = power_num * base_num
        exp_num = exp_num-1
    return power_num

def main():
    '''
    Main function starts here
    '''
    input_num = input()
    input_num = input_num.split()
    print(iter_power(float(input_num[0]), int(input_num[1])))

if __name__ == "__main__":
    main()
