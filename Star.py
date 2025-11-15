from turtle import *
import random

# Setup
speed(0)
bgcolor("black")
hideturtle()

# Draw Moon (Crescent Shape)
penup()
goto(-50, 50)
pendown()
color("white")
begin_fill()
circle(30)
end_fill()

penup()
goto(-40, 60)
pendown()
color("black")
begin_fill()
circle(30)
end_fill()

# Draw Stars using only loops and basic commands
color("white")
for _ in range(10):  # Draw 10 stars
    penup()
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    goto(x, y)
    pendown()

    for _ in range(5):  # Draw a simple star
        forward(10)
        right(144)

done()
