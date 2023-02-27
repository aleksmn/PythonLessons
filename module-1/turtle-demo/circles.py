import turtle
import random

turtle.setup(900, 900)
turtle.shape("turtle")
turtle.color("#E96479")
turtle.bgcolor('#4D455D')


# Примеры:
# turtle.circle(100)

# turtle.left(90)
# turtle.forward(50)

# turtle.dot(100)


# Гипнокруги

turtle.speed(8)
turtle.hideturtle()
# turtle.width(2)

size = 5

for i in range(1, 160):
    turtle.circle(size * i)

    turtle.left(20)


# Гипнокруги

# Устанавливаем размеры окна
# turtle.speed(50)
# size = 5

# for i in range(0, 160):
#     turtle.circle(size)
#     turtle.left(5)
#     size += 10


turtle.mainloop()
