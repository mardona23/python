import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(600,700)
t=turtle.Turtle()
numberside=8
length=100
angle=360/numberside
for i in range(numberside):
    t.forward(length)
    t.right(angle)
turtle.done()