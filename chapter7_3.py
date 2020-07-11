import math

def estimate_pi():
	k = 1
	while True:
		last_term = (math.factorial(4*k)*(1103 + 26390*k)) / (math.factorial(k)**4)*(396**(4*k))
		estimate = last_term * (2*math.sqrt(2)/9801)
		print (estimate)
		k = k + 1
		if last_term == 1e-10:
			break
estimate_pi()
