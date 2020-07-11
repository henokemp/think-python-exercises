def is_triangle ():
	a = int(input('Input for a:\n'))
	b = int(input('Input for b:\n'))
	c = int(input('Input for c:\n'))
	if a + b == c or a + c == b or b + c == a:
		print("Yes")
	else:
		print("No")

is_triangle()
