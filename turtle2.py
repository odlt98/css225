import turtle
wn = turtle.Screen()
roger = turtle.Turtle()

SideNumber = int(input("How many sides for your polygon? ")) 
SideLength = int(input("What length do you want the sides? "))
#LineColor = str(input("What color for the lines of your polygon? "))
#fColor = str(input("What color to fill your polygon? "))

for x in range(SideNumber):
#   roger.color(LineColor)
    roger.forward(SideLength)
    roger.left(360/SideNumber)
