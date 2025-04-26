import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(600,700)
t=turtle.Turtle(4)
numberside=10
length=100
angle=360/numberside
for i in range(numberside):
    t.forward(length)
    t.right(angle)
turtle.done()