import turtle

turtle.shape('turtle')

turtle.color('cyan')
turtle.bgcolor('black')
# Скорость (1-10)
turtle.speed(2)
# Размеры окна
turtle.setup(0.5, 0.95)

# Рисование круга
turtle.dot(100)
turtle.forward(200)
turtle.dot(100)
turtle.back(400)
turtle.dot(100)
turtle.goto(0, 0)
turtle.goto(100, 150)
turtle.dot(100)
turtle.goto(0, 0)
turtle.goto(-100, 150)
turtle.dot(100)
turtle.goto(0, 0)
turtle.goto(100, -150)
turtle.dot(100)
turtle.goto(0, 0)
turtle.goto(-100, -150)
turtle.dot(100)




turtle.mainloop()