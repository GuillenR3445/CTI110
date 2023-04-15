# CTI-110
# P4LAB1b
# Ruben Guillen
# 15 Apr 2023

# This program uses turtle to draws my initials

# Import turtle and assigns it
import turtle
wn = turtle.Screen()  # creates a playground for turtles
wn.bgcolor("black") # changes color of background
t = turtle.Turtle() 

# add some display options
t.pensize(5)            # increase pensize (takes integer)
t.pencolor("red")     # set pencolor (takes string)
t.shape("arrow")    # set shape ("arrow", "turtle", "circle", "square", "triangle", "classic")

# draws first initial
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(135)
t.forward(70.71)

# moves the turtle over to a new position
t.penup()
t.goto(175, 100)
t.pendown()

# draws second initial
t.right(135)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)

# hide the turtle
turtle.hideturtle()

# wait for the user to close the window
wn.mainloop()