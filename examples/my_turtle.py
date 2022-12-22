
import turtle

turtle.bgcolor('black')

loadWindow = turtle.Screen()

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

t = turtle.Pen()

t.speed(9)

for i in range(100):

    # t.pencolor('white')

    t.pencolor(colors[i % 6])

    t.circle(5*i)
    t.circle(-5*i)
    t.left(i)

turtle.exitonclick()
