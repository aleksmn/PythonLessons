import turtle
import random


def draw_retangle(x, y, w, h, color):
    turtle.up()
    turtle.seth(0)
    turtle.goto(x-w/2, y-h/2)
    turtle.fillcolor(color)
    turtle.down()
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(w)
        turtle.left(90)
        turtle.fd(h)
        turtle.left(90)
    turtle.end_fill()

draw_retangle(0, 0, 200, 100, 'red')


turtle.mainloop()