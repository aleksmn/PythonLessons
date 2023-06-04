x = 5
y = 1000

# Логическое И  (ИСТИНА оба условия)
if x > 0 and y > 500:
    print("OK")

# Логическое ИЛИ
if x > 0 or y == "hello" and x > y:
    print("OK-2")




# Даны 3 целых числа a, b и c. Выведи количество одинаковых чисел.


# a, b, c = 7, 0, 10

# if a == b and a == c and c == b:
#     print(3)
# elif a != b and a != c and c != b:
#     print(1)
# else:
#     print(2)


# Даны 3 числа a, b и c. Необходимо найти наибольшее из них.

# a, b, c = 7, 1, 2

# if a > b and a > c:
#     maximum = a
# elif b > a and b > c:
#     maximum = b
# elif c > a and c > b:
#     maximum = c
# else:
#     maximum = None

# print(maximum)


# В программу вводится год — year. Определи, является ли он високосным. Выведи 1, если является, иначе — 0.


# # Год високосный, если он делится на 4 без остатка И не делится на 100 без остатка, ИЛИ, если он делится без остатка на 400.


# year = int(input("Введите год: "))


# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(1)
# else:
#     print(0)


# Даны год, месяц и день рождения 2-ух людей. Необходимо определить, кто из них старше.


y1, m1, d1 = 1995, 7, 31
y2, m2, d2 = 1995, 8, 18


# if y1 > y2:
#     print(2)
# elif y1 < y2:
#     print(1)
# else:
#     if m1 < m2:
#        print(1)
#     elif m1 > m2:
#         print(2)
#     else:
#         if d1 < d2:
#             print(1)
#         elif d1 > d2:
#             print(2)
#         else:
#             print("возраста равны")


# Способ 2


y1, m1, d1 = 1994, 8, 17
y2, m2, d2 = 1995, 7, 18

if y1 == y2 and m1 == m2 and d1 == d2:
    print(0)

elif y1 == y2 and m1 == m2:
    if d1 > d2:
        print(2)
    else:
        print(1)

elif y1 == y2:
    if m1 > m2:
        print(2)
    else:
        print(1)

else:
    if y1 > y2:
        print(2)
    else:
        print(1)

















