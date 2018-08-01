varA = 1
varB = 2
if ((type(varA) is str) or (type(varB) is str)):
	print("Strings involved")
elif ((varA) > (varB)):
	print("Bigger")
elif ((varA) == (varB)):
	print("equal")
else:
	print("Smaller")