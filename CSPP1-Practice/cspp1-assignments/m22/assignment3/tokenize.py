'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    string = (string.split())
    string = (' '.join(e for e in string if e.isalpha())).split()
    print(string)
            
def main():
    num_lines = int(input())
    for i in range(num_lines):
    	input_str = input()
    	tokenize(input_str)
if __name__ == '__main__':
    main()
