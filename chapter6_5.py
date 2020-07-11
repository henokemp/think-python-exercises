def gcd (a, b):
	if a == b: 
		return a
	if a > b: 
		return gcd(a-b,b)
	if a < b:
		return gcd(a, b-a)

print(gcd(1234, 3421))