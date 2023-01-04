import turtle

turtle.color('red')
turtle.bgcolor('black')
turtle.speed(2)

turtle.shape('turtle')
# 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'


for x in range(8):
    turtle.forward(100)
    turtle.left(45)

turtle.mainloop()
