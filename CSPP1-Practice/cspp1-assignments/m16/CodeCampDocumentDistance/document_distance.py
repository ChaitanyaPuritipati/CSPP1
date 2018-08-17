'''
    Document Distance - A detailed description is given in the PDF
'''
import math
def distance_calculator(common_dict):
    numerator = 0
    sqr_1 = 0
    sqr_2 = 0
    for k in common_dict:
        numerator = numerator + (common_dict[k][0])*(common_dict[k][1])
        sqr_1 = sqr_1 + (common_dict[k][0])**2.0
        sqr_2 = sqr_2 + (common_dict[k][1])**2.0
    sqr_1 = math.sqrt(sqr_1)
    sqr_2 = math.sqrt(sqr_2)
    denominator = (sqr_1)*(sqr_2)
    output = numerator/denominator
    return output

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = dict1.lower()
    dict2= dict2.lower()
    dict1 = dict1.split(". ")
    dict2 = dict2.split(". ")
    for i in range(len(dict1)):
        dict1[i] = dict1[i].split(" ")
    for j in range(len(dict2)):
        dict2[j] = dict2[j].split(" ")
    for i in range(len(dict1)):
        for j in range(len(dict1[i])):
            #print(dict1[i][j])
            dict1[i][j] = ''.join(e for e in dict1[i][j] if e.isalpha())
            #if ' ' in dict1[i][j]:
            #    dict1[i][j] = dict1[i][j].split(' ')
            #    dict1[i][j] = ''.join(e for e in dict1[i][j])
    for i in range(len(dict2)):
        for j in range(len(dict2[i])):
            #print(dict2[i][j])
            dict2[i][j] = ''.join(e for e in dict2[i][j] if e.isalpha())
            #if ' ' in dict2[i][j]:
            #    dict2[i][j] = dict2[i][j].split(' ')
            #    dict2[i][j] = ''.join(e for e in dict2[i][j])            
    stop_words = load_stopwords("stopwords.txt")
    dict1_new = []
    for i in range(len(dict1)):
        for j in range(len(dict1[i])):
            #print(dict1[i][j])
            if dict1[i][j] not in stop_words:
            #    if dict1[i][j] != ' ':
                   dict1_new.append(dict1[i][j])
    dict1 = dict1_new
    dict2_new = []
    for i in range(len(dict2)):
        for j in range(len(dict2[i])):
            #print(dict2[i][j])
            if dict2[i][j] not in stop_words:
            #    if dict2[i][j] != ' ':
                    dict2_new.append(dict2[i][j])
    dict2 = dict2_new
    common_dict = {}
    for i in dict1:
        if i in common_dict:
            common_dict[i][0] = common_dict[i][0] + 1
        else:
            common_dict[i] = [1, 0]
    for j in dict2:
        if j not in dict1:
            common_dict[j] = [0, 1]
        elif j in common_dict:
            common_dict[j][1] = common_dict[j][1] + 1
    common_dict.pop('', None)
    #print(list(common_dict.keys()))     
    print(len(common_dict))
    print(distance_calculator(common_dict))
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
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
    (similarity(input1, input2))

if __name__ == '__main__':
    main()
