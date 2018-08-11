'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    data = data.splitlines()
    output_dict = {}
    #print(data)
    ln = len(data)
    #print(ln)
    for j in range(ln):
    	if "follows" in data[j]:
    		data[j] = data[j].split(" follows ")
    		#print(data[j])
    		temp = data[j][0]
    		#print(data[j][1])
    		data[j][1] = data[j][1].split(",")
    		#print(data[j][1])
    		if temp in output_dict:
    			output_dict[temp].append(data[j][1])
    		else:
    			output_dict[temp] = list(data[j][1])	
    return output_dict		
    #data = data.split()
    #print(data)


def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    #print(string)    
    print(create_social_network(string))

if __name__ == "__main__":
    main()
