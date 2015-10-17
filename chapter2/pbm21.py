'''Problem 21: Write a program wrap.py that takes filename 
and width as aruguments and wraps the lines longer than width.'''

def wrap(filename,width):
	list = open(filename).readlines()
	for x in list:
		if(len(x)<=30):
			print x
		else:
			print x[:30]
			print x[30:]