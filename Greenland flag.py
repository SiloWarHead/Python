from turtle import *
hideturtle()
speed(0)
bgcolor("black")

color("red")
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(80)
    left(90)
end_fill()

penup()
goto(0, 80)
pendown()

color("white")
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(80)
    left(90)
end_fill()

penup()
goto(140,79)
pendown()

color("red")
left(90)
begin_fill()
circle(50,180)
end_fill()

color("white")
begin_fill()
circle(50,180)
end_fill()
