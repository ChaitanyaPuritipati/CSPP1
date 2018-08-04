'''
Author: Puritipati Chaitanya Prasad Reddy
Date: 4-8-2018
File: 20186018_CSPP1_week1_exam_special_char.py
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    length_str = len(str_input)
    str_output = ""
    for i in range(length_str):
        if str_input[i] in "!@#$%^&*":
            str_output = str_output + " "
        else:
            str_output = str_output + str_input[i]
    print(str_output)
if __name__ == "__main__":
    main()
