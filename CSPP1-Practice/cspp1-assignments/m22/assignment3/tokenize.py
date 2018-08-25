'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string, output_dict):
    '''
    Tokenize function starts here
    '''
    string = (string.split())
    for every_ele in string:
        every_ele = every_ele.strip('",;.')
        if every_ele in output_dict:
            output_dict[every_ele] += 1
        else:
            output_dict[every_ele] = 1
    return output_dict
def main():
    '''
    Main Function starts here
    '''
    output_dict = {}
    num_lines = int(input())
    for iter_num in range(num_lines):
        input_str = input()
        output_dict = tokenize(input_str, output_dict)
        iter_num += 1
    print(output_dict)
if __name__ == '__main__':
    main()
