from turtle import *

tracer(0)
screensize(1000, 1000)  # Уменьшите размер экрана

r = 20

lt(90)

rt(30)
for i in range(3):
    rt(150)
    fd(6*r)
    rt(30)
    fd(12*r)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(2, "red")

update()
mainloop()