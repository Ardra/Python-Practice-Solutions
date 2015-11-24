'''Problem 8: Write a function count_change to count the number of ways to  
change any given amount. Available coins are also passed as argument to the function.'''

def count_change(n, lst):
	if n == 0:
       	 	return 1
    	if n < 0 or len(lst) == 0:
        	return 0
    	return count_change(n, lst[1:]) + count_change(n-lst[0], lst)

print count_change(10, [1, 2])

