'''Problem 11: Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.'''
import sys
import zipfile

directory = sys.argv[1]
z = zipfile.zipfile(directory,'w')
length = len(sys.argv)
for i in range(2,length):
    z.write(sys.argv[i])
