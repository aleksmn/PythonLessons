import turtle

turtle.color('red')
turtle.bgcolor('black')
turtle.speed(10)

turtle.shape('turtle')


n = 6  # форма лепестков
k = 7  # количество лепестков

for i in range(k):
    # Шестиугольник
    for x in range(n):
        turtle.forward(100)
        turtle.left(360/n)
    # Поворот
    turtle.left(360/k)







turtle.mainloop()
