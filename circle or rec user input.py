from turtle import *
hideturtle()
speed(0)

rad = float(input("Enter radius: "))
circle(rad)

penup()
goto(0, -300)
pendown()

l = float(input("Enter length: "))
w = float(input("Enter width: "))

for i in range(2):
    forward(l)
    left(90)
    forward(w)
    left(90)
