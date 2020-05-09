import turtle
import math

bob = turtle.Turtle()

# bob.getscreen().bgcolor("black")
bob.color("red", "yellow")
bob.speed(0)

ox = -500
oy = 0


def drawTriangle(a1, a2, s1, s2, h, directionRotate):
	if directionRotate == "right":
		a1 = 360 - a1
		a2 = 360 - a2
	bob.forward(s1)
	if a2 > 180:
		bob.left(a2 + 1)
	else:
		bob.left(a2 - 1)
	bob.penup()
	bob.forward(h)
	bob.pendown()
	if a2 > 180:
		bob.left(a2 + 1)
	else:
		bob.left(a2 - 1)
	bob.forward(s2)
	if a1 > 180:
		bob.left(a1 + 1)
	else:
		bob.left(a1 - 1)
	bob.forward(s1)

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


def drawSquare(s1, directionRotate):
	a1 = 91
	if directionRotate == "right":
		a1 = 360 - a1

	# for j in range(0, 3):
	# 	bob.forward(s1)
	# 	if a1 > 180:
	# 		bob.left(a1 + 1)
	# 	else:
	# 		bob.left(a1 - 1)

	# bob.forward(s1)

	i = 0
	while s1 > 8:
		bob.left(a1)
		bob.forward(s1)
		i = i + 1;
		s1 = s1 - s1/54



# First triangle - start
s1 = 300
s2 = 300
h = s1 * math.sqrt(2)
a1 = 91
a2 = 136

bob.penup()
bob.goto(ox, oy)
bob.pendown()

drawTriangle(a1, a2, s1, s2, h, "left")
# First triangle - end

# Second triangle - start

bob.penup()
bob.goto(ox + s1, oy + s2)
bob.pendown()
bob.setheading(0)
bob.right(90)

drawTriangle(a1, a2, s1, s2, h, "right")
# Second triangle - end


# Third triangle - start

bob.penup()
bob.goto(ox + s1*2, oy + s2)
bob.pendown()
bob.setheading(0)
bob.right(90)

drawTriangle(a1, a2, s1, s2, h, "left")
# Third triangle - end


# Fourth triangle - start

bob.penup()
bob.goto(ox + s1*3, oy)
bob.pendown()
bob.setheading(0)
bob.right(180)

drawTriangle(a1, a2, s1, s2, h, "right")
# Fourth triangle - end


# Fifth triangle - start

bob.penup()
bob.goto(ox, oy)
bob.pendown()
bob.setheading(0)

drawTriangle(a1, a2, s1, s2, h, "right")
# Fifth triangle - end


# Sixth triangle - start

bob.penup()
bob.goto(ox + s1, oy - s1)
bob.pendown()
bob.setheading(0)
bob.left(90)

drawTriangle(a1, a2, s1, s2, h, "left")
# Sixth triangle - end


# Seventh triangle - start

bob.penup()
bob.goto(ox + s1*3, oy)
bob.pendown()
bob.setheading(0)
bob.right(180)

drawTriangle(a1, a2, s1, s2, h, "left")
# Seventh triangle - end


# Eighth triangle - start

bob.penup()
bob.goto(ox + s1*2, oy - s2)
bob.pendown()
bob.setheading(0)
bob.left(90)

drawTriangle(a1, a2, s1, s2, h, "right")
# Eighth triangle - end


# First square - start
s1 = 300
a1 = 91

bob.penup()
bob.goto(ox + s1, oy + s1)
bob.pendown()
bob.setheading(0)

bob.forward(s1)
bob.right(a1-1)
bob.forward(s1)
bob.right(a1-1)
bob.penup()
bob.forward(s1)
bob.pendown()
bob.right(a1-1)
bob.forward(s1)

drawSquare(s1, "right")
# First square - end

# Second square - start

bob.penup()
bob.goto(ox + s1, oy)
bob.pendown()
bob.setheading(0)

bob.penup()
bob.forward(s1)
bob.pendown()
bob.right(a1-1)
bob.forward(s1)
bob.right(a1-1)
bob.forward(s1)
bob.right(a1-1)
bob.forward(s1)

drawSquare(s1, "right")
# Second square - end

bob.hideturtle()
turtle.done()