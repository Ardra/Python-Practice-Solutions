def grep(word, filename):
	found = False
	list = open(filename).readlines()
	for x in list:
		if(word in x):
			print x.strip('\n')
