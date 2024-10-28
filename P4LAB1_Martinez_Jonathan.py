# Jonathan Martinez
# 10/28/2024
# P4LAB1
# Use loops to make a square using turtle

# Import turtle libary to use in the code
import turtle

# Set up the window and turtle option
window = turtle.Screen()
timmy = turtle.Turtle()

timmy.pensize(6)
timmy.pencolor("green")
timmy.shape("arrow")

# while loop to draw 4 sides of a square
line = 0
while line < 4:
    timmy.right(90)
    timmy.forward(150)
    line += 1

#For loop to draw the triangle
for line1 in range (3):
    timmy.left(120)
    timmy.forward(150)
