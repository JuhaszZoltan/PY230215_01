import turtle
from random import randint

t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(10)

for x in range(360):
    red = f'{randint(0, 255):02x}'
    green = f'{randint(0, 255):02x}'
    blue = f'{randint(0, 255):02x}'
    t.pencolor(f'#{red}{green}{blue}')
    t.width(2)
    t.forward(x)
    t.left(43)

turtle.done()