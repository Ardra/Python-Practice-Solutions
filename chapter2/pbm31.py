'''Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.'''

def parse(filename,seperator,comment_indicator):
	outer_list = open(filename).readlines()
	result = []
 	for x in outer_list:
		if(x[:1]!=comment_indicator):
			result.append(x.strip('\n').split(seperator))
	return result