import turtle

turtle.bgcolor('black')
turtle.color('white')

turtle.speed(2)

turtle.title('Set Heading')

my_font = ('sans-serif', 14)

turtle.setheading(0)


turtle.forward(80)

turtle.write("East", font=my_font)

turtle.home()

# Указываем направление
turtle.setheading(90)

turtle.forward(80)
turtle.write("North", font=my_font)


turtle.home()


turtle.seth(180)


turtle.forward(80)
turtle.write("West", align="right", font=my_font)


turtle.home()


turtle.setheading(270)


turtle.forward(80)
turtle.write("South", font=my_font)



turtle.hideturtle()


turtle.mainloop()