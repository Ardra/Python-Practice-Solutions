'''Problem 5: Write a function tree_reverse to reverse elements of
 a nested-list recursively.'''

def tree_reverse(seq):
	result = []
    	for x in seq:
		if isinstance(x, list):
			result.append(tree_reverse(x))
		else:
			result.append(x)
	result.reverse()
	return result
print tree_reverse([[1, 2], [3, [4, 5]], 6])