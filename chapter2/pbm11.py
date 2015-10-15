def dups(list):
	new_list=[]
	dup_list=[]
	for x in list:
		if not(x in new_list):
			new_list.append(x)
		else:
			dup_list.append(x)
	return dup_list

