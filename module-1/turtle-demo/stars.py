import turtle
import random


turtle.setup(1920, 1080)

turtle.speed(0)
turtle.hideturtle()

turtle.bgcolor('black')
turtle.color('white')


for i in range(10000):
    turtle.penup()
    turtle.goto(random.randint(-(1920/2), (1920/2)), random.randint(-(1080/2), (1080/2)))
    turtle.pendown()
    turtle.color(random.random(), random.random(), random.random())
    turtle.dot(random.randint(1,6))

turtle.mainloop()