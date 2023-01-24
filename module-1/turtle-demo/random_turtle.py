import turtle
import random


turtle.color('blue')
turtle.bgcolor('black')
turtle.speed(3)
turtle.shape('circle')


colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

turtle.color(random.choice(colors))
turtle.begin_fill()

for i in range(20):

    turtle.goto((random.randint(-300, 300), random.randint(-300, 300)))


turtle.end_fill()
turtle.mainloop()

