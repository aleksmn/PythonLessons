
# Напиши программу, которая находит сумму всех чисел от 1 до number, которые делятся на 3. 
# number является положительным целым числом.



# number = 35

# res = 0

# for x in range(1, number + 1):
#     if x % 3 == 0:
#         print(x)
#         res = res + x
#         print(res)

# print("Итог:", res)







# Дано натуральное число N. Вычисли:


# 1**1 - 2**2 + 3**3 - 4** 4 + ... + N


n = 7

res = 0

for x in range(1, n + 1):

    if x % 2 == 0:
        res -= x**x
    else:
        res += x**x

print(res)








# Дано натуральное число N. Вычисли:

# 1! + 2! + ... + n!


# Нахождение факториала числа
n = 5

res = 1

for x in range(1, n+1):
    res = res * x

print(res)














x = int(input('Введите число: '))

fact_sum = 0


for n in range(1, x+1):

    fact = 1
    # Вложенный цикл
    for i in range(1, n+1):
        fact = fact * i

    fact_sum += fact


print(fact_sum)



    



