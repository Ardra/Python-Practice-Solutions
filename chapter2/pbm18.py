'''Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.'''
def head(lines, filename):
    list = open(filename).readlines()
    for i in range(lines):
        print list[i].strip('\n')

def tail(lines, filename):
    list = open(filename).readlines() 
    #print list
    i=len(list)
    j= i-lines
    for x in range(j,i):
	print list[x].strip('\n')
    

