import turtle


n = int(input("Введите число: "))

turtle.setup(900, 900)
turtle.shape("turtle")
turtle.color("#6527BE")
turtle.bgcolor('#A7EDE7')

for k in range(n*2):
	turtle.left(180/n)
	for i in range(0, n):
		turtle.forward(100)
		turtle.right(360/n)



# После цикла
turtle.hideturtle()
turtle.mainloop()