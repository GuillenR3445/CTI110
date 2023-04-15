# CTI-110
# P4LAB1a
# Ruben Guillen
# 15 Apr 2023

# This program uses turtle to draw a square and triangle

# import turtle and change shape of turtle
import turtle
wn = turtle.Screen()  # creates a playground for turtles
t = turtle.Turtle() 
t.shape("turtle")

# draws the square
for i in range(4):
    t.forward(50)
    t.left(90) # angle of turn

# moves the turtle over to a new position
t.penup()
t.goto(100, 0)
t.pendown()

# draws the triangle
for i in range(3):
    t.forward(50)
    t.left(120) # angle of turn

# hide the turtle
turtle.hideturtle()

# wait for the user to close the window
wn.mainloop()