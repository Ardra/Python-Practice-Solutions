#reverse a list without slicing
def reverse(list):
	new_list=[]
	for i in range(len(list)-1,-1,-1):
		new_list.append(list[i])
	return new_list