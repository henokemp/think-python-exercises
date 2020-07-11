"""def ack (m, n):
	if m == 0:
		n = n + 1
		print (m, n)
	if n == 0:
		m = m - 1
		n = 1 
		ack (m, n)
		print (m, n)
	if m > 0 and n > 0:
		return ack(m-1, ackermann(m,n-1)) 
	
ack(3, 4)"""

def ackermann (m, n):
	if m == 0:
		print (m, n)
		return n + 1
	if n == 0:
		return ackermann(m-1, 1)
	print (m, n)
	return ackermann(m-1, ackermann(m,n-1))

print(ackermann(3, 4))
