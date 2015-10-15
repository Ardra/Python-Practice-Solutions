def group(list, number):
	new_list = []
	i=0
	j=number
	while(i<len(list)):
		new_list.append(list[i:j])
		i=i+number
		j=j+number
	return new_list
	