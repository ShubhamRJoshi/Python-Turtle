import turtle
import math

bob = turtle.Turtle()

bob.getscreen().bgcolor("black")
bob.color("red", "yellow")
bob.speed(3)

bob.penup()
# bob.goto((-200),-200)
bob.pendown()

l = 300
diff = 10
r = (int)(l/diff)
bob.forward(l)
bob.left(120)
bob.forward(l)
bob.left(120)
bob.forward(l)

while l > 8:
	l = l - l/25
	bob.left(121)
	bob.forward(l)


turtle.done()