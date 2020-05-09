import turtle
import math

bob = turtle.Turtle()

# bob.getscreen().bgcolor("black")
bob.color("red", "yellow")
bob.speed(10)

ox = -100
oy = -150

bob.penup()
bob.goto(ox, oy)
bob.pendown()

# First triangle
s1 = 300
s2 = 300
h = s1 * math.sqrt(2)
a1 = 91
a2 = 136

bob.forward(s1)
bob.left(135)
bob.penup()
bob.forward(h)
bob.pendown()
bob.left(135)
bob.forward(s2)
bob.left(90)
bob.forward(s1)

# s2 = s2 - s2/35
# s1 = s1 - s1/20
# h = h - h/25

h = h - h/60
s2 = s2 + 2
s1 = s1 - s1/100


i = 0
while s1 > 8:
	if i%3 == 0:
		bob.left(a2)
		bob.forward(h)
	elif i%3 == 1:
		bob.left(a2)
		bob.forward(s2)
	else:
		bob.left(a1)
		bob.forward(s1)
	i = i + 1;
	s1 = s1 - s1/25
	s2 = s2 - s2/25
	if i < 3:
		h = h - h/30
	else:
		h = h - h/25

# Second triangle
s1 = 300
s2 = 300
h = s1 * math.sqrt(2)

bob.penup()
bob.goto(ox + s1, oy + s2)
bob.pendown()
bob.setheading(0)
bob.right(90)

bob.forward(s1)
bob.right(135)
bob.penup()
bob.forward(h)
bob.pendown()
bob.right(135)
bob.forward(s2)
bob.right(90)
bob.forward(s1)

h = h - h/60
s2 = s2 + 2
s1 = s1 - s1/100

i = 0
while s1 > 8:
	if i%3 == 0:
		bob.right(a2)
		bob.forward(h)
	elif i%3 == 1:
		bob.right(a2)
		bob.forward(s2)
	else:
		bob.right(a1)
		bob.forward(s1)
	i = i + 1;
	s1 = s1 - s1/25
	s2 = s2 - s2/25
	if i < 3:
		h = h - h/30
	else:
		h = h - h/25

bob.penup()
turtle.done()