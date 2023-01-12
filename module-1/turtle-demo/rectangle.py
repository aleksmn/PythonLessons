import turtle
import random


def draw_rectangle(x, y, w, h, color):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x-w/2, y-h/2)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.end_fill()





rand_color = (random.random(), random.random(), random.random())

print(rand_color)


draw_rectangle(0, 0, 200, 100, rand_color)



turtle.mainloop()