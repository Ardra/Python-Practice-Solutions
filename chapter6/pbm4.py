'''Problem 4: Write a function treemap to map a function over nested list.
>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]'''


def treemap(key, seq):
	result = []    
    	for x in seq:
		if isinstance(x, list):
            		result.append(treemap(key, x))
		else:
            		result.append(key(x))
	return result
print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])

	