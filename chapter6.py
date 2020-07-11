import math

def compare (x, y):
	if x > y:
		return 1
	if x == y:
		return 0
	if x < y:
		return -1

compare (4,3)

def hypotenuse (a, b):
	return math.sqrt(a**2 + b**2)

def is_between (x, y, z):
	return x <= y <= z



