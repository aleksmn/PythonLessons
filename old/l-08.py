# Дано целое трёхзначное число a. Выведи количество чётных цифр в данном числе


# a = 268

# a = str(a)

# a1 = int(a[0])
# a2 = int(a[1])
# a3 = int(a[2])

# n = 0

# print(a1, a2, a3)

# if a1 % 2 == 0:
#     n += 1
# if a2 % 2 == 0:
#     n += 1
# if a3 % 2 == 0:
#     n += 1

# print("Количество четный чисел:", n)


# Даны 4 числа a, b, c и d. Одно из них отлично от оставшихся, равных друг другу. Необходимо вывести данное число.

# a, b, c, d = 5, 1, 1, 1

# print(a, b, c, d)


# if a != b and a != c and a != d:
#     print(a)

# if b != a and b != c and b != d:
#     print(b)

# if c != a and c != b and c != d:
#     print(c)

# if d != a and d != b and d != c:
#     print(c)


# Даны две различные клетки шахматного поля,
# каждая из которых задаётся двумя числами, — координата по x, координата по y.
# Выведи 1, если шахматный король сможет перейти с первой клетки на вторую одним ходом, иначе выведи 0.


# try:
#     # Где король стоял
#     x1 = int(input("x1 = "))
#     y1 = int(input("y1 = "))

#     # Куда делаем ход
#     x2 = int(input("x2 = "))
#     y2 = int(input("y2 = "))

# except:
#     print("Неверный ввод!")
#     quit()

# diff_x = abs(x1 - x2)
# diff_y = abs(y1 - y2)


# if diff_x > 1 or diff_y > 1:
#     print(0, "Ход не возможен")

# elif diff_y == 0 and diff_x == 0:
#     print('Ход не сделан')

# else:
#     print(1, "Ход возможен")


# Даны две различные клетки шахматного поля, каждая из которых задаётся двумя числами, — координата по xx, координата по yy. Выведи 11, если шахматный ферзь сможет перейти с первой клетки на вторую одним ходом, иначе выведи 00.


# try:
#     x1 = int(input("x1 = "))
#     y1 = int(input("y1 = "))

#     x2 = int(input("x2 = "))
#     y2 = int(input("y2 = "))

# except:
#     print("Неверный ввод координат")
#     quit()


# diff_x = abs(x1 - x2)
# diff_y = abs(y1 - y2)


# # print(diff_x, diff_y)


# if diff_x == diff_y:
#     print(1)

# elif diff_y == 0 or diff_x == 0:
#     print(1)

# else:
#     print(0)




# Ход ферзя

# x1 = int(input("x1 = "))
# y1 = int(input("y1 = "))


# x2 = int(input("x2 = "))
# y2 = int(input("y2 = "))


# if x1 - y1 == x2 - y2 or (x1 == x2 or y1 == y2):
#     print(1)
# else:
#     print(0)