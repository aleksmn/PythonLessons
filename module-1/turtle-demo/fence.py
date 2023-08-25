import turtle

turtle.color("white")
turtle.bgcolor("black")

turtle.speed(10)

turtle.penup()
turtle.back(400)
turtle.pendown()

for i in range(0, 40):
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)

turtle.forward(10)

# Спрятать черепашку
turtle.hideturtle()

turtle.mainloop()