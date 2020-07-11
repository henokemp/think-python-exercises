import math
import time

length_year = 60*60*24*365.25

def conversion ():
	year = 1970 + (time.time() / (length_year))
	month = (year - int(year)) * (366)
	"""day = 
	hour =
	minute = 
	second = """

	print (time.time())
	print (year)
	print (month)

conversion ()