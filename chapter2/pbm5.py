def product(list):
	product=1
	for x in list:
		product=product*x
	return product
def factorial(number):
	if number==0:
		return 1
	else:
		list=range(1,number+1)
		return product(list)