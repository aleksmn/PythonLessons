import turtle
import random

turtle.setup(900, 900)
turtle.shape("turtle")
turtle.color("#E96479")
turtle.bgcolor('#4D455D')


for i in range(10):
    turtle.goto(random.randint(-350, 350), random.randint(-350, 350))

    turtle.begin_fill()

    side = random.randint(10, 100)
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.end_fill()





turtle.mainloop()
