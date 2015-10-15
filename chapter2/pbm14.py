def unique(list,key=lambda s:s.lower()):
	lower_list=[]
	for x in list:
		lower_list.append(key(x))
	new_list=[]
	for x in lower_list:
		if not(x in new_list):
			new_list.append(x)
	return new_list