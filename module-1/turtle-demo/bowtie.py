import turtle


turtle.color("#E96479")
turtle.bgcolor('#4D455D')

turtle.speed(2)
turtle.shape('classic')



turtle.begin_fill()


turtle.goto(100, 100)
turtle.goto(100, -100)
turtle.goto(-100, 100)
turtle.goto(-100, -100)
turtle.goto(0, 0)

turtle.end_fill()

turtle.mainloop()

