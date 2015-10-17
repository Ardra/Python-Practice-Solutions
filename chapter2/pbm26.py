'''Problem 26: Python provides a built-in function filter(f, a) 
that returns items of the list a for which f(item) returns true.
 Provide an implementation for filter using list comprehensions.'''

def my_filter(function,list):
	return [x for x in list if f(x)==True]