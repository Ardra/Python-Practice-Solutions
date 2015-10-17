'''Problem 23: Write a program center_align.py to center align all lines in the given file'''
import sys
line_length = 80
list = open(sys.argv[1]).readlines()
#print list
for x in list:
	length = len(x)
	space = (line_length - length)/2
	str = ""
	for i in range(0,space):
		str = str+" "
	print str+x