import math

def mysqrt(a):
	x = 1
	while True:
		y = (x + a / x) / 2.0
		if y == math.sqrt(a):
			break
		x = y
	print (y)

def test_square_root(a):
	print (a)
	mysqrt(a)
	
test_square_root(7)