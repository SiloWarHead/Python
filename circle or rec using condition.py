from turtle import *
hideturtle()
speed(3)

want = input("What do you want to draw (circle/rectangle/square)? ")

if want == "circle":
    rad = float(input("Enter radius: "))
    c = input("Enter color: ")
    color(c)
    fc = input("Enter fillcolor: ")
    fillcolor(fc)
    begin_fill()
    circle(rad)
    end_fill()
elif want == "rectangle":
    ln = float(input("Enter length: "))
    wd = float(input("Enter width: "))
    c = input("Enter color: ")
    color(c)
    fc = input("Enter fillcolor: ")
    fillcolor(fc)
    begin_fill()
    for i in range(2):
        forward(ln)
        left(90)
        forward(wd)
        left(90)
    end_fill()
elif want == "square":
    sd = float(input("Enter side: "))
    for i in range(4):
        forward(sd)
        left(90)

else:
    print("Invalid Keyword!")
