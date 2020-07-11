def is_power(a,b):
	if a % b == 0 and a / b % b == 0:
		return True
	return False
print (is_power(9, 3))