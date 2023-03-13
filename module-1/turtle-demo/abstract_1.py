import turtle
import random

turtle.setup(900, 900)
turtle.shape("classic")
turtle.color("#E96479")
turtle.bgcolor('#4D455D')
turtle.width(2)

# Перемещаемся на случайную точку для начала рисунка
turtle.penup()
turtle.goto(random.randint(-350, 350), random.randint(-350, 350))
turtle.pendown()

# Напишем функцию для рисования квадрата


def draw_square():
    turtle.begin_fill()
    # Рисуем квадрат со стороной side
    side = random.randint(10, 100)
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.end_fill()


# Приступаем к созданию картины

n = 10    # Количество квадратов

for i in range(n-1):
    draw_square()
    turtle.goto(random.randint(-350, 350), random.randint(-350, 350))


draw_square()
# Прячем черепашку
turtle.hideturtle()

# Основной цикл
turtle.mainloop()
