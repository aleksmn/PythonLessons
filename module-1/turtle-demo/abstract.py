import turtle
from random import randint

turtle.screensize(500, 500)
turtle.shape("turtle")
turtle.pencolor("blue")
turtle.fillcolor("blue")

for i in range(10):
    turtle.goto(randint(-250, 250), randint(-250, 250))
    side = randint(10, 100)

    turtle.begin_fill()
    for j in range(4):
        turtle.forward(side)
        turtle.right(90)

    turtle.end_fill()

turtle.mainloop()
