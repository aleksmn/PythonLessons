import turtle
import random


def draw_rectangle(x, y, w, h, color):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x-w/2, y-h/2)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.end_fill()


turtle.setup(700, 700)
turtle.title("Random Rectangles")
turtle.speed(0)
turtle.hideturtle()
n = 100
for i in range(n):
    draw_rectangle(random.randint(-300, 300), random.randint(-300, 300),
                  random.randint(5, 100), random.randint(5, 100),
                  (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))


turtle.mainloop()
