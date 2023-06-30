import turtle

turtle.setup(900, 900)
turtle.shape("turtle")
turtle.color("#6527BE")
turtle.bgcolor('#A7EDE7')

for i in range(0, 10):
	turtle.right(36)
	for i in range(0, 5):
		turtle.forward(100)
		turtle.right(72)

turtle.hideturtle()
turtle.mainloop()