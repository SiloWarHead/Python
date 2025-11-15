from turtle import *

hideturtle()
speed(0)
pensize(5)

hideColors = "ndfredvmgreenbsbluecyanmdslime"

green = hideColors[8:13]
blue = hideColors[15:19]
cyan = hideColors[19:23]
lime = hideColors[26:30]

colors = [green, blue, cyan, lime]

side = int(input("Enter one side of the square: "))

for color in colors:
    pencolor(color)
    forward(side)
    right(90)

done()
