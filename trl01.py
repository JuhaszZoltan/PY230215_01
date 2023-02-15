import turtle

t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(10)

#           0        1       2        3         4         5
szinek = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']

for x in range(360):
    t.pencolor(szinek[x%4])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(92)

turtle.done()