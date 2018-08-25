'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
	output_str = ""
    for e in string:
    	if e not in '!@#$%^&*':
            output_str += e
    return output_str        


def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
