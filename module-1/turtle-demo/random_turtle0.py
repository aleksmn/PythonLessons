import turtle
import random

# from svg_turtle import SvgTurtle

# turtle = SvgTurtle(900, 900)

turtle.setup(900, 900)
turtle.hideturtle()

turtle.color("black")
turtle.bgcolor("#E8E2E2")
turtle.shape('turtle')
turtle.speed(20)
# Список цветов
colors = ['#2B3467', '#804674', '#B3E5BE', '#FF0303', '#E96479', '#F99417', '#5D3891']

turtle.width(4)


for i in range(30):
    # Перемещаем черепашку в случайную точку
    # Получаем случайные координаты
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    turtle.penup()

    size = random.randint(6, 160)

    turtle.goto(x-size/2, y-size/2)
    # Рисуем квадрат!
    turtle.pendown()

    # Меняем цвет на случайный из списка
    turtle.fillcolor(random.choice(colors))


    # Начинаем заливку
    turtle.begin_fill()


    n = 4
    # turtle.left(random.randint(1, 360))
    turtle.setheading(-15)
    for i in range(n):
        
        turtle.forward(size)
        turtle.left(360/n)

    # Завершаем заливку
    turtle.end_fill()




# Последняя строка
# turtle.mainloop()

# Сохранение в файл
# turtle.save_as('example.svg')