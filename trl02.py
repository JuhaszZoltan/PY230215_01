import turtle
from random import randint

t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(10)

#           0        1       2        3         4         5
szinek = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']

for x in range(360):
    t.pencolor(szinek[randint(0, len(szinek) - 1)])
    t.width(2)
    t.forward(x)
    t.left(60)

turtle.done()