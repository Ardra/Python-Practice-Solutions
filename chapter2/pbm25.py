'''Problem 25: Python provides a built-in function map
that applies a function to each element of a list. 
Provide an implementation for map using list comprehensions.'''


def my_map(function,list):
	return [function(x) for x in list]