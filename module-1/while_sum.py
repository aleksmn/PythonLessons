n = int(input("Введите число: "))

summa = 0
k = 0

while n > 0:
    d = n % 10
    summa += d

    n = n // 10
    k += 1


print("Сумма цифр:", summa)
print("Количество цифр:", k)