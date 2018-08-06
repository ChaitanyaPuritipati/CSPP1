'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 6-8-2018
'''
def paying_debt(balance_num, annual_interest_rate, guess_num):
    '''
    Function is to calculate the remaining balance in a year
    '''
    balance_temp = balance_num
    i = 1
    while i <= 12:
        mir_num = annual_interest_rate/12      
        mub_num = balance_temp - guess_num
        balance_temp = mub_num + (mir_num*mub_num)
        i = i+1
    return balance_temp

def paying_debt_in_year(balance_num, annual_interest_rate):
    '''
    Function to calculate lowest payment
    '''
    balance_temp = balance_num
    approx_num = 0.01
    mir_num = annual_interest_rate/12.0
    high_val = (balance_num * (1 + mir_num)**12) / 12.0
    low_val = balance_num/12
    middle_val = (low_val + high_val) / 2.0
    while abs(paying_debt(balance_temp, annual_interest_rate, middle_val)) >= approx_val:
        if approximation_val < paying_debt(balance_temp, annual_interest_rate, middle_val):            
            low_val = middle_val
        else:
            high_val = middle_val
        middle_val = (low_val + high_val) / 2.0  
    k_num = middle_val
    return "Lowest Payment: "+str(round(k_num, 2))
def main():
    '''
    Main function starts here
    '''
    input_num = input()
    input_num = input_num.split(' ')
    input_num = list(map(float, input_num))
    print(paying_debt_in_year(input_num[0], input_num[1]))    
if __name__ == "__main__":
    main()
