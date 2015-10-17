'''Problem 24: Provide an implementation for zip function using list comprehensions.'''
def zip(list1,list2):
	return [(list1[i],list2[i]) for i in range(len(list1))]