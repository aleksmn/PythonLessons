import turtle
import random


turtle.color('blue')
turtle.bgcolor('black')
turtle.speed(3)
turtle.shape('circle')


colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

turtle.color(random.choice(colors))


for i in range(1000):



    turtle.goto((random.randint(-200, 200), random.randint(-200, 200)))



turtle.mainloop()

