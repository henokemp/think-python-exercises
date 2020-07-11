import math
import turtle

bob = turtle.Turtle()

def koch(turtle, length):
    if length < 3:
        turtle.fd(length)
        return
    koch(turtle, length/3)
    turtle.lt(60)
    koch(turtle, length/3)
    turtle.rt(120)
    koch(turtle, length/3)
    turtle.lt(60)
    koch(turtle, length/3)

koch(bob, 1000)