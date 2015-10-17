def wrap(filename,width):
	list = open(filename).readlines()
	for x in list:
		if(len(x)<=30):
			print x
		else:
			sentence = x.split()
			count = 0 
			length = 0
			i = 0
			str = " "
			while(length<= width) and i<=len(sentence):
				count = count + 1
				length = length + len(sentence[i])+1
				str = str + sentence[i]+ " "
				i = i+1
				
			print str
			for i in range(count, len(sentence)):
				print sentence[i]+" "

				