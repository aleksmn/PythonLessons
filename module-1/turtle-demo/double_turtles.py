import turtle
import random


t1 = turtle.Turtle()
t2 = turtle.Turtle()

turtle.bgcolor('black')

t1.shape('turtle')
t2.shape('circle')


t1.color('red')
t2.color('blue')

t1.forward(100)

t2.left(90)
t2.forward(100)




for i in range(20):

    t1.goto((random.randint(-300, 300), random.randint(-300, 300)))
    t2.goto((random.randint(-300, 300), random.randint(-300, 300)))

turtle.mainloop()

