'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

# #def tokenize(string):
# 	output_dict = {}

#     for every_ele in string:
#     	if every_ele in output_dict:
#     		output_dict[every_ele] += 1
#     	else:
#     	    output_dict[every_ele] = 1	
#     return output_dict
def main():
    num_lines = int(input())
    for i in range(num_lines):
    	input_str = input()
    	input_str = (input_str.split())
        input_str = (' '.join(e for e in input_str if e.isalpha())).split()
    print(input_str)    
if __name__ == '__main__':
    main()
