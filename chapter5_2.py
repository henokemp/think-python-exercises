import math

"""Fermat's Last Theorem says that there are no positive integers a, b, and c such that 
	a**n + b**n = c**n for any values of n greater than 2. 
1. Write a function named check_fermat that takes four parameters -- a, b, c, and n -- 
and checks to see if Fermat's theorem holds. If n is greater than 2 and a**n + b**n = c**n 
the program should print, "Holy smokes, Fermat was wrong!" Otherwise the program should print,
"No, that doesn't work."""

def check_fermat (a, b, c, n):
	if a**n + b**n == c**n == true and n > 2:
		print ("Holy smokes, Fermat was wrong!")
	else:
		print ("No, that doesn't work.")

def check_fermat_custom():
	a = int(input('Value for a?\n'))
	b = int(input('Value for b?\n'))
	c = int(input('Value for c?\n'))
	n = int(input('Value for n?\n'))
	return check_fermat(a, b, c, n)

check_fermat_custom()
