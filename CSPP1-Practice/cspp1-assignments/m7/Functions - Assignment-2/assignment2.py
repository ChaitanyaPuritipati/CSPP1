'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 6-8-2018
'''
def paying_debt(balance_num, annual_interest_rate, guess_num):
    '''
    Function to calculate the remaining balance
    '''
    balance_temp = balance_num
    i = 1
    while i <= 12:
        mir_num = annual_interest_rate/12      
        mub_num = balance_temp - guess_num
        balance_temp = mub_num + (mir_num*mub_num)
        i += 1
    return balance_temp

def paying_debt_in_year(balance_num, annual_interest_rate):
    '''
    function to calculate minimum monthly payments
    '''
    balance_temp = balance_num
    aprroximation_val = 0.1
    step_val = 1
    guess_num = 0.0
    while paying_debt(balance_temp, annual_interest_rate, guess_num*10) >= aprroximation_val:      
        guess_num += step_val
         
    
    round_num = round(guess_num)
    return "Lowest Payment: "+str(round_num*10)
def main():
    '''
    Main Function starts here
    '''
    input_num = input()
    input_num = input_num.split(' ')
    data = list(map(float, input_num))
    print(paying_debt_in_year(input_num[0], input_num[1]))
    
if __name__ == "__main__":
    main()