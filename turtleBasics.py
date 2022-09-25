import turtle 
from math import sqrt
from random import randrange

#Define the turtle
bob = turtle.Turtle()

#Turtle Speed
bob.speed(1)

#Turtle Color
bob.color("blue")#we can use #000000 (RGB codes)

#Moving
# bob.forward(100)
# bob.left(90)
# bob.forward(100)

#make square
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)

#Fill inside the square
# bob.color("blue", "green")#for inside color
# bob.begin_fill()
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.end_fill()

#Make a space
# bob.penup()
# bob.forward(100)
# bob.pendown()
# bob.forward(100)

#Make a flower
# bob.color("purple","yellow")
# bob.speed(10)
# bob.begin_fill()
# for i in range(100):
#     bob.forward(sqrt(i)*20)
#     bob.left(170)
# bob.end_fill()

#Random Drawin something
# bob.color("purple")
# bob.speed(10)
# for i in range(100):
#     i = randrange(0,10)
#     bob.forward(sqrt(i)*20)
#     bob.left(170)

#something weird
# for i in range(100):
#     bob.forward(sqrt(i)*10)
#     bob.left(45)

#For stop the turtle
turtle.done()