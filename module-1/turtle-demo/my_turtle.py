import turtle

turtle.bgcolor('black')

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

turtle.speed(9)

for i in range(100):

    turtle.color(colors[i % 6])

    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)


turtle.mainloop()
