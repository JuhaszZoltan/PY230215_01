import turtle
from random import randint

(w, h) = turtle.screensize()
turtle.bgcolor('black')
turtle.speed(10)

pens:list[turtle.Pen] = []

for i in range(12):
    pens.append(turtle.Pen())
    red = f'{randint(0, 255):02x}'
    green = f'{randint(0, 255):02x}'
    blue = f'{randint(0, 255):02x}'
    pens[i].pencolor(f'#{red}{green}{blue}')
    pens[i].pencolor()
    pens[i].width(2)
    pens[i].penup()
    pens[i].setpos(randint(-w, w), randint(-h, h))
    pens[i].left(randint(0, 360))
    pens[i].pendown()

for x in range(100):
    for p in pens:
        p.forward(x*1.5)
        p.left(88)

turtle.done()