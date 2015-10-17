'''Problem 30: Write a python function parse_csv to parse csv (comma separated values) files.'''

def parse_csv(filename):
	outer_list = open(filename).readlines()
	result = []
 	for x in outer_list:
		result.append(x.strip('\n').split(','))
	return result