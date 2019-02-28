import turtle

#Omar De La Torre
#2/28/2019

def drawSquare(t, sz):
        for i in range(4):
            t.forward(sz)
            t.left(90)

wn = turtle.Screen
redd = turtle.Turtle()
redd.color("red")

size = [20, 40, 60, 80, 100, 120, 140,160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]

for x in size:
        drawSquare(redd, x)
        redd.penup()
        redd.backward(10)
        redd.right(90)
        redd.forward(10)
        redd.left(90)
        redd.pendown()




