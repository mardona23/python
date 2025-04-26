import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(900,900)
t=turtle.Turtle()
numberside=2
length=150
angle=360/numberside
for i in range(numberside):
    t.forward(length)
    t.left(angle)
turtle.done()