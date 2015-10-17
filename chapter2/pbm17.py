'''Problem 17: Write a program reverse.py to print lines of a file in reverse order.'''
import sys
list = open(sys.argv[1]).readlines()
new_list = list[::-1]
for x in new_list:
    print x.strip('\n')
