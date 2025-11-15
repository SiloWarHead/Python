from turtle import *
hideturtle()
speed(0)
pensize(10)
penup()
forward(-240)
pendown()

colors = ["green", "cyan", "red", "orange", "blue"]

for i in colors:
    fillcolor(i)
    begin_fill()
    circle(50)
    end_fill()
    penup()
    forward(110)
    pendown()
