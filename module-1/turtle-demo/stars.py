import turtle
import random


turtle.setup(1200, 600)

turtle.speed(0)
turtle.hideturtle()

turtle.bgcolor('black')
turtle.color('white')


for i in range(1000):
    turtle.penup()
    turtle.goto(random.randint(-500, 500), random.randint(-280, 280))
    turtle.pendown()
    turtle.dot(random.randint(1,5))

turtle.mainloop()