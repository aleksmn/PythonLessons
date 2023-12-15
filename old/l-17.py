

def print10(s):
    print(s*10)



print10("Привет")







n = input("Введите число: ")

h = len(n) // 2

summa1 = 0
summa2 = 0

for i in range(h):
    summa1 += int(n[i])
    summa2 += int(n[-(i + 1)])


# После цикла
print(summa1)
print(summa2)
