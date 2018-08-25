'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string, output_dict):
    string = (string.split())
    string = (' '.join(e for e in string if e.isalpha())).split()
    print(string)
    print(output_dict)
    for every_ele in string:
    	if every_ele in output_dict:
    		output_dict[every_ele] += 1
    	else:
    	    output_dict[every_ele] = 1	
    return output_dict
def main():
    output_dict = {}
    num_lines = int(input())
    for i in range(num_lines):
    	input_str = input()
    	output_dict = tokenize(input_str, output_dict)
    return output_dict
if __name__ == '__main__':
    main()
