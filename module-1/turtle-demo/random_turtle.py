import turtle
import random


turtle.color('blue')
turtle.bgcolor('black')
turtle.speed(4)
turtle.shape('circle')


colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

turtle.color(random.choice(colors))

# Функция

def get_rand_coords(a, b):
    return (random.randint(a, b), random.randint(a, b))



for i in range(1000):
    
    turtle.goto(get_rand_coords(-200, 200))



turtle.mainloop()

