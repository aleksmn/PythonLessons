import turtle
import random

turtle.setup(900, 900)
turtle.hideturtle()

turtle.color("#E96479")
# turtle.bgcolor('#4D455D')
turtle.bgcolor("#E8E2E2")
turtle.shape('turtle')
turtle.speed(20)
# Список цветов
colors = ['#2B3467', '#804674', '#B3E5BE', '#FF0303', '#E96479', '#F99417', '#5D3891']


for i in range(30):
    # Перемещаем черепашку в случайную точку
    # Получаем случайные координаты
    x = random.randint(-350, 350)
    y = random.randint(-350, 350)

    turtle.penup()
    turtle.goto(x, y)
    # Рисуем квадрат!
    turtle.pendown()

    # Меняем цвет на случайный из списка
    turtle.color(random.choice(colors))


    # Начинаем заливку
    turtle.begin_fill()

    size = random.randint(10, 100)

    n = 4
    turtle.left(random.randint(1, 360))
    for i in range(n):
        
        turtle.forward(size)
        turtle.left(360/n)

    # Завершаем заливку
    turtle.end_fill()







# Последняя строка
turtle.mainloop()
