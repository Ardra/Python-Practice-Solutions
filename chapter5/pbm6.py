'''Problem 6: Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.'''
import sys
import os

def linecount(dir):
    files = os.listdir(dir)
    python_files=[]
    for f in files:
        if '.py' in f:
            python_files.append(f)
    
    for file in python_files:
        count = 0
        for line in open(file).readlines():
            if line[0]!='#' and line!='\n':
                count=count+1
        print file,count
linecount(sys.argv[1])
