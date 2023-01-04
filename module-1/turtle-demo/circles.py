import turtle
import random

turtle.shape()
turtle.color('red')
turtle.bgcolor('black')




# turtle.dot(100)
# turtle.forward(100)
# turtle.circle(50)

### Гипнокруги

# Устанавливаем размеры окна
turtle.Screen().setup(1920, 1080)
turtle.speed(50)
size = 5

for i in range(0, 160):
    turtle.circle(size)
    turtle.left(5)
    size += 10


turtle.mainloop()
