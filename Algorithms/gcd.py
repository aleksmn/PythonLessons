# Найти НОД - наибольший общий делитель двух чисел а и б

# НОД(a, b) = НОД(a-b, b)


# Наивный способ
a = 12
b = 18



gcd = 1
for i in range(2, max(a-b, b)):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)




