'''Problem 2: Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.'''
import sys
files=[]
for i in range(1,len(sys.argv)):
    files.append(sys.argv[i])

def printline(files):
    for file in files:
        for line in open(file):
            if len(line)>40:
                print line
printline(files)
