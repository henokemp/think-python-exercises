def breaks():
	print ('+ - - - - + - - - - + - - - - + - - - - +')

def lines():
	print ('|         |         |         |         |')

def do_four(func):
	func()
	func()
	func()
	func()

def print_grid():
	breaks()
	do_four(lines)
	breaks()
	do_four(lines)

print_grid()
print_grid()
breaks()