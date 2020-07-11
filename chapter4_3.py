import turtle
import math

bob = turtle.Turtle()
print(bob)

def pie(t, side, n):
	centre_angle_turn = 180.0 - (360.0 / n)
	distant_angle_turn = 180.0 - (centre_angle_turn / 2.0)
	opposite = side * math.sin(centre_angle_turn * math.pi / 180)
	for i in range(n):
		t.fd(side)
		t.lt(distant_angle_turn)
		t.fd(opposite)
		t.lt(distant_angle_turn)
		t.fd(side)
		t.lt(180)

pie(bob, 100, 60)

turtle.mainloop()