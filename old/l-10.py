
# Цикл FOR


# 1, 3, 5 

# for x in range(1, 50, 2):

#     print(f"Число {x} в квадрате:  {x ** 2}")



# n = 5

# res = 0

# for x in range(1, n+1):
#     res = res + x
#     print(res)

# print("Итог")
# print(res)












# n = int(input("Введите число: "))

# print("Таблица квадратов до", n, "включительно")

# # создаем переменную "копилку"
# summa = 0

# for x in range(1, n+1):

#     print(f'{x}² = {x**2}', end=' ')

#     summa = summa + x**2

#     if x % 5 == 0:
#         print()



# print("Сумма квадратов:", summa)














# a = int(input("Число 1: "))
# b = int(input("Число 2: "))


# if a > b:
#     print("Неверный ввод")
#     quit()


# for x in range(a, b+1):
# 	print(x)


# Дано натуральное число N. Вычисли:
# 1 + 2 + 3 + ... + N

# n = 75

# sum = 0

# for x in range(1, n+1):
#     sum = sum + x
#     print('Число:', x, '  Сумма:', sum)


# print("---------------------------")
# print("Итог:", sum)


# Даны два целых числа a и b, причём a ≤ b. Выведи сумму всех чётных чисел от a до b.


# print("Сумма четных чисел от a до b, включительно")

# a = int(input("a = "))
# b = int(input("b = "))

# sum = 0

# for n in range(a, b+1):
#     if n % 2 == 0:
#         sum = sum + n


# print("---------------------------")
# print("Итог: ", sum)


# Дано натуральное число N. Вычисли:
# 1/2/3/.../N.


# n = 7

# res = 1

# for i in range(2, n+1):
#     res = res / i

#     print("Число", i, "  Результат деления:", res)


# Дано натуральное число N. Вычисли:

# 1 ^ 1 + 2 ^ 2 + 3 ^ 3 + ... + N ^ N

# n = 7

# res = 0

# for i in range(1, n+1):
#     res = res + i ** i

#     print("Число", i, "  Результат:", res)


# Напиши программу, которая находит сумму всех 
# чисел от 1 до number, которые делятся на 3. 
# number является положительным целым числом.

# number = int(input("Введите число: "))

# summa = 0

# for x in range(1, number + 1):
#     if x % 3 == 0:
#         print(x)
#         summa = summa + x

# print("---------")
# print("Сумма равна:", summa)


# 5
# 1 2 3 4 5

# 1 / 2 / 3 / 4 / 5


# n = 5 

# res = 1


# for x in range(1, n+1):
#     res = res / x


# print(res)