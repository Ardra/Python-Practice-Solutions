'''Problem 28: Write a function enumerate that takes a list and 
returns a list of tuples containing (index,item) for each item in the list.'''

def enumerate(list):
	return [ (i,list[i]) for i in range(0,len(list))]