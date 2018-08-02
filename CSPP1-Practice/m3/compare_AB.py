'''

Author: Chaitanya Prasad Reddy Puritipati
@Date: 01-08-2018

'''

VARA = 1
VARB = 2
if ((isinstance(VARA) is str) or (isinstance(VARB) is str)):
    print("Strings involved")
elif VARA > VARB:
    print("Bigger")
elif VARA == VARB:
    print("equal")
else:
    print("Smaller")
