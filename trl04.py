import turtle
from random import randint

lorem:list[str] = open('lorem.txt').readlines()[0].split(' ')

t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(10)

for x in range(len(lorem)):
    red = f'{randint(0, 255):02x}'
    green = f'{randint(0, 255):02x}'
    blue = f'{randint(0, 255):02x}'
    t.pencolor(f'#{red}{green}{blue}')
    t.width(2)
    t.penup()
    t.forward(x*(x/36)+1)
    t.pendown()
    t.write(lorem[x], font=('Times New Roman', int(x / 12 + 1), 'bold'))
    t.left(44)
turtle.done()