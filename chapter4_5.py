import math
import turtle

writer = turtle.Turtle()
print(writer)

def draw_a(t):
	t.lt(60)
	t.fd(100)
	t.rt(120)
	t.fd(100)
	t.lt(180)
	t.fd(50)
	t.lt(60)
	t.fd(50)
	t.lt(180)
	t.fd(50)
	t.rt(60)
	t.fd(50)
	t.lt(60)
	t.pu()
	t.fd(20)

draw_a(writer)

turtle.mainloop()