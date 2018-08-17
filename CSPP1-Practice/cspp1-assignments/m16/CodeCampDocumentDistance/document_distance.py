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
    dict1 = dict1.split(",")
    dict2 = dict2.split(",")
    
    #print(type(dict1))
    #print(type(dict2))
    #dict1 = dict1.strip(" ")
    #dict2 = dict2.strip(" ")
    #for i in range(len(dict1)):
        #dict1[i] = dict1[i].strip(" ")
    #for j in range(len(dict2)):
        #dict2[j] = dict2[j].strip(" ")    
    #dict1 = dict1.split(",")
    #dict2 = dict2.split(",")
    print(dict1)
    print(dict2) 

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
