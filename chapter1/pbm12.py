def count_digits(x):
	count = 0
	while( x > 0):
		x = x / 10
		count = count + 1
	return count
#print count_digits(5)
#print count_digits(12345)

