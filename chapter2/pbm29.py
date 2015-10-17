'''Problem 29: Write a function array to create an 2-dimensional array. 
The function should take both dimensions as arguments. Value of each 
element can be initialized to None:'''

def array(row,col):
	list = []
	for i in range(row):
		list.append([None]*col)
	return list
	