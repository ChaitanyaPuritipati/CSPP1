'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = dict1.lower()
    dict2= dict2.lower()
    #print(dict1)
    #print(dict2)
    #dict1 = dict1.strip()
    #dict2 = dict2.strip()
    #print(dict1, "before")
    dict1 = dict1.split(". ")
    dict2 = dict2.split(". ")
    
    #print(type(dict1))
    #print(type(dict2))
    #dict1 = dict1.strip(" ")
    #dict2 = dict2.strip(" ")
    for i in range(len(dict1)):
        dict1[i] = dict1[i].split(" ")
    for j in range(len(dict2)):
        dict2[j] = dict2[j].split(" ")
    for i in range(len(dict1)):
        for j in range(len(dict1[i])):
            dict1[i][j] = dict1[i][j].strip(",.!@#$%^&*?")
            if "'" in dict1[i][j]:
                dict1[i][j] = dict1[i][j].split("'")
                dict1[i][j] = ''.join(e for e in dict1[i][j])
    for i in range(len(dict2)):
        for j in range(len(dict2[i])):
            dict2[i][j] = dict2[i][j].strip(",.!@#$%^&*?")
            if "'" in dict2[i][j]:
                dict2[i][j] = dict2[i][j].split("'")
                dict2[i][j] = ''.join(e for e in dict2[i][j])            
    stop_words = load_stopwords("stopwords.txt")
    for i in range(len(dict1)):
        dict1_new = []
        for j in range(len(dict1[i])):
            if dict1[i][j] not in stop_words:
                dict1_new.append(dict1[i][j])        
    dict1 = dict1_new
    print(dict1)         

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
    #print(input1)
    #print(input2)
    (similarity(input1, input2))

if __name__ == '__main__':
    main()
