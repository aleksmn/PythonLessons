import turtle
import random

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t1.color('pink')
t2.color('cyan')
t3.color('magenta')
t1.speed(4)
t2.speed(4)
t3.speed(4)

# Размеры окна
turtle.setup(600, 600)
turtle.bgcolor('#4D455D')

# 10 раз перейти в случайную точку
for m in range(100): 
    # Перемещаемся в случайную точку
    t1.goto(random.randint(-300, 300), random.randint(-300, 300))
    t2.goto(random.randint(-300, 300), random.randint(-300, 300))
    t3.goto(random.randint(-300, 300), random.randint(-300, 300))






# Основной цикл
turtle.mainloop()