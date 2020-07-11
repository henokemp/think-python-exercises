import turtle
import math

bob = turtle.Turtle()
t = turtle.Turtle()
print(bob)
print(t)

def square(name, length): # look how the syntax for defining the function and calling the function is similar
	for i in range(4):
		name.fd(length)
		name.lt(90)
	
def polygon(name, length, n):
	for i in range(n):
		name.fd(length)
		name.lt(360/n)

def circle(t, r):
	circumference = 2 * math.pi * r
	n = 50
	length = circumference / n
	polygon (t, length, n)

def arc(t, r, angle):
	circumference = 2 * math.pi * r
	n = 50
	length = circumference / n
	polygon (t, length, n * (angle/360))

arc(t, 100, 360)
turtle.mainloop()