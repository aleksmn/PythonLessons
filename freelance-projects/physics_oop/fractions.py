# Сокращение дроби
# Функция для нахождения наибольшего общего делителя двух чисел
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Функция для сокращения дроби
def simplify_fraction(num, den):
    # Находим наибольший общий делитель числителя и знаменателя
    common = gcd(num, den)

    # Сокращаем дробь
    num = num // common
    den = den // common

    return num, den

# Пример использования
num = 6
den = 12

simplified_num, simplified_den = simplify_fraction(num, den)
print(simplified_num, "/", simplified_den)  # Вывод: 1 / 2