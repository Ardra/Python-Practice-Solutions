def cumulative_sum(list):
	sum=0
	new_list=[]
	for x in list:
		sum=sum+x
		new_list.append(sum)
	return new_list
