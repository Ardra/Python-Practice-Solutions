def istrcmp(x,y):
	str1=x.upper()
	str2=y.upper()
	length=len(str1)
	comparison = True
	for i in range(length):
		if(str1[i]!=str2[i]):
			return False
	return True