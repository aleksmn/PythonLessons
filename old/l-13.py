# # 1 1 2 3 5 8 13 21

# n = int(input("Введите число: "))

# fib1 = 1
# fib2 = 1

# while fib1 <= n:
#     print(fib1)
#     temp = fib1
#     fib1 = fib2
#     fib2 = temp + fib2

# print(fib1)
# temp = fib1
# fib1 = fib2
# fib2 = temp + fib2




# a = int(input("a = "))
# b = int(input("b = "))


# counter = 0
# while a > b:
#     a = a - b
#     print(a)
#     counter += 1

# print("Деление нацело:", counter)
# print("Остаток:", a)






# Дано натуральное число N. Если оно является простым, то следует вывести 1, иначе — 0.

# n = 35
# d = 2

# k = 0

# while d < n:
#     print(f"Число: {n}  Делитель:  {d}")
#     print("Результат деления: ", n / d)
#     print("Остаток от деления: ", n % d)
#     print("------------------")

#     if n % d == 0:
#         k = k + 1

#     d = d + 1

# if k < 1:
#     print("Число простое")
# else:
#     print("Число не простое")
#     print("Количество делителей: ", k + 2)


# Дано натуральное число N. Если оно является простым, то следует вывести 1, иначе — 0.

# n = 35
# d = 2

# k = 0

# while d < n:
#     print(f"{n = } {d = }")
#     print(f"{n / d = }", )
#     print("Остаток от деления: ", n % d)
#     print("------------------")

#     if n % d == 0:
#         k = k + 1

#     d = d + 1

# if k < 1:
#     print("Число простое")
# else:
#     print("Число не простое")
#     print("Количество делителей: ", k + 2)


# n = 19
# d = 2

# k = 0

# while d < int(n ** 0.5) + 1:
#     print(f"{n = } {d = }")
#     print(f"{n / d = }", )
#     print("Остаток от деления: ", n % d)
#     print("------------------")

#     if n % d == 0:
#         k = k + 1

#     d = d + 1

# if k < 1:
#     print("Число простое")
# else:
#     print("Число НЕ простое")









# Перевернуть число используя // и %



# n = 321

# # нужно получить 123
# # 100 + 20 + 3

# res = 0

# while n > 0:
#     remainder = n % 10
#     res = (res * 10) + remainder
#     n = n // 10

# print('Перевернутое число:', res)