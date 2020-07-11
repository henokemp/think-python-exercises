import math
import turtle

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r):
    arc_length = 2 * math.pi * r * abs(180) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(180) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def spiral (t, r):
	arc(t,r)
	for i in range(10):
		r = r*math.pi
		arc(t, r)

spiral(bob, 10)

turtle.mainloop()