import turtle


turtle.color('red')
turtle.bgcolor('black')
turtle.speed(2)
turtle.shape('classic')

turtle.fillcolor("red")

turtle.begin_fill()


turtle.goto(100, 100)
turtle.goto(100, -100)
turtle.goto(-100, 100)
turtle.goto(-100, -100)
turtle.goto(0, 0)

turtle.end_fill()

turtle.mainloop()

