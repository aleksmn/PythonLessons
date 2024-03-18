import turtle
import random

turtle.setup(900, 900)
turtle.shape("turtle")
turtle.pensize(3)


# Создадим список цветов
colors = ["green", "red", "blue", "aqua", "purple"]


# Исходные координаты
y = -100
x = -100

# Переходим в начальную точку
turtle.penup()
turtle.goto(x, y)
turtle.pendown()

for i in range(15):

    # Случайный цвет
    turtle.color(random.choice(colors))

    turtle.forward(200)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    y += 20







# Основной цикл
turtle.mainloop()