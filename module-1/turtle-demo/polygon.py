import turtle


n = int(input("Введите количество сторон: "))
l = int(input("Введите длину стороны: "))

# Настраиваем черепашку

turtle.color('orange')
turtle.bgcolor('black')

turtle.hideturtle()
turtle.speed(100)

# Размеры окна
turtle.Screen().setup(1920, 1080)

# Меняем начальное расположение
turtle.penup()
turtle.setx(0)
turtle.sety(400)
turtle.pendown()



for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)


turtle.mainloop()
