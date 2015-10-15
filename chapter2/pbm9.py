def cumulative_product(list):
	product=1
	new_list=[]
	for x in list:
		product=product*x
		new_list.append(product)
	return new_list
