def unique(list):
	new_list=[]
	for x in list:
		if not(x in new_list):
			new_list.append(x)
	return new_list