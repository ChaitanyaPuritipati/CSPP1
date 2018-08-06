'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 6-8-2018
'''
def paying_debt_in_year(balance_num, annual_interest_rate, monthly_payment_rate):
	'''
	Function is to calculate the remaining balance
	'''
	balance_temp = balance_num
	i = 1
	while i <= 12:
		mir_num = annual_interest_rate / 12.0
		mmp_num = monthly_payment_rate*balance_temp
		mub_num = balance_temp - mmp_num
		balance_temp = mub_num + (mir_num*mub_num)
		i += 1
	return "Remaining balance: "+str(round(balance_temp, 2))
def main():
	'''
	Main Function starts here
	'''
	input_num = input()
	input_num = input_num.split(' ')
	input_num = list(map(float, input_num))
	print(paying_debt_in_year(input_num[0], input_num[1], input_num[2]))

if __name__ == "__main__":
	main()

