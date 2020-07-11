x = 9

def find_x(n):
	if not isinstance(n, int): # Lines 4 and 5 are a guardian to make sure that the given value is an integer.
		print ('n has to be a whole number.')
		return None
	elif n != x:
		print (n)
		n = n + 1
		find_x(n)
	else:
		print(n)

find_x(1)
