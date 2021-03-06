'''
    Author: Puritipati Chaitanya Prasad Reddy
    Date: 18-08-2018
    EXAM WEEK 3
    Roll no: 20186018
    -----------------------------------------------------------------------------------------
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''

# helper function to load the stop words from a file
def load_stopwords():
    '''
        loads stop words from a file and returns a dictionary
    '''
    filename = "stopwords.txt"
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    ln_text = len(text)
    for line in range(ln_text):
        text[line] = text[line].lower().split()
        for word in range(len(text[line])):
            text[line][word] = text[line][word].strip("!@#$%^&*.,?;").split("'")
            text[line][word] = (''.join(map(str, text[line][word])))
    #print(text)
    return text
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    stop_words = load_stopwords()
    docs = word_list(docs)
    index_dict = {}
    ln_docs = len(docs)
    for line_index in range(ln_docs):
        line_dict = {}
        for word in range(len(docs[line_index])):
            if docs[line_index][word] in line_dict:
                line_dict[docs[line_index][word]] += 1
            else:
                line_dict[docs[line_index][word]] = 1
        for key in line_dict:
            if key not in stop_words:
                if key in index_dict:
                    value_tuple = (line_index, line_dict[key])
                    index_dict[key].append(value_tuple)
                else:
                    index_dict[key] = []
                    value_tuple = (line_index, line_dict[key])
                    index_dict[key].append(value_tuple)
    return index_dict
# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
    #print(documents)
    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
