from turtle import *

hideturtle()
speed(0)

def drawCircle(rad):
    circle(rad)

def drawRec(ln, wd):
    for i in range(2):
        forward(ln)
        left(90)
        forward(wd)
        left(90)

want = input("What do you want to draw (circle/rectangle): ")

if want == "circle":
    r = float(input("Enter radius: "))
    drawCircle(r)
elif want == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    drawRec(l, w)
else:
    print("Invalid keyword!")
