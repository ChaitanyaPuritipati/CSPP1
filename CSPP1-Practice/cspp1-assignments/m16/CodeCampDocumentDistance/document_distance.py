'''
    Document Distance - A detailed description is given in the PDF
'''
import math
def distance_calculator(common_dict):
    '''
    Function to calculate the plagirised value
    '''
    numerator = 0
    sqr_1 = 0
    sqr_2 = 0
    for k in common_dict:
        numerator = numerator + (common_dict[k][0])*(common_dict[k][1])
        sqr_1 = sqr_1 + ((common_dict[k][0])**2)
        sqr_2 = sqr_2 + ((common_dict[k][1])**2)
    sqr_1 = math.sqrt(sqr_1)
    sqr_2 = math.sqrt(sqr_2)
    denominator = (sqr_1)*(sqr_2)
    output = numerator/denominator
    return output
def no_stop_words(dict2, stop_words):
    '''
    Function to remove stop_words
    '''
    dict2_new = []
    ln_dict_2 = len(dict2)
    for i in range(ln_dict_2):
        for j in range(len(dict2[i])):
            if dict2[i][j] not in stop_words:
                dict2_new.append(dict2[i][j])
    return dict2_new
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = dict1.lower().split(". ")
    dict2 = dict2.lower().split(". ")
    ln_dict_1 = len(dict1)
    ln_dict_2 = len(dict2)
    for i in range(ln_dict_1):
        dict1[i] = dict1[i].split(" ")
    for j in range(ln_dict_2):
        dict2[j] = dict2[j].split(" ")
    for i in range(ln_dict_1):
        for j in range(len(dict1[i])):
            dict1[i][j] = ''.join(e for e in dict1[i][j] if e.isalpha())
    for i in range(ln_dict_2):
        for j in range(len(dict2[i])):
            dict2[i][j] = ''.join(e for e in dict2[i][j] if e.isalpha())

    stop_words = load_stopwords()
    dict1 = no_stop_words(dict1, stop_words)
    dict2 = no_stop_words(dict2, stop_words)
    common_dict = {}
    for i in dict1:
        if i in common_dict:
            common_dict[i][0] = common_dict[i][0] + 1
        else:
            common_dict[i] = [1, 0]
    for j in dict2:
        if j in common_dict:
            common_dict[j][1] = common_dict[j][1] + 1
        else:
            common_dict[j] = [0, 1]
    common_dict.pop('', None)
    return (distance_calculator(common_dict))
def load_stopwords():
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    filename = "stopwords.txt"
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
