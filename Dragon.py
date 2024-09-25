import turtle

def dragon_curve(t, length, level, direction):
    if level == 0:
        t.forward(length)
    else:
        t.right(direction * 45)
        dragon_curve(t, length / (2 ** 0.5), level - 1, 1)
        t.left(direction * 90)
        dragon_curve(t, length / (2 ** 0.5), level - 1, -1)
        t.right(direction * 45)

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Set up initial position and color
t.penup()
t.goto(-200, 0)
t.pendown()
t.pensize(2)
t.pencolor("blue")

# Draw the dragon curve
order = 10  # Number of iterations (level)
length = 400  # Length of the curve
dragon_curve(t, length, order, 1)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
