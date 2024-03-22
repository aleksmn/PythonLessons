# Цикл FOR

# Выведем все числа от 25 до 50 включительно
# Найдем сумму этих чисел

a = 25
b = 50

result = 0

for i in range(a, b+1):
    print(i)
    # Увеличиваем сумму на i
    result += i


print("Сумма", result)
