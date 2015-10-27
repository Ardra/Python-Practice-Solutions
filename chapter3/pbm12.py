'''Problem 12: Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.'''
import sys
__import__(sys.argv[1])

print help(sys.argv[1])

