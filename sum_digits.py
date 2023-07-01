n = 123456

# Найти сумму всех цифр

# 1. Способ (% //)

res = 0

while n > 0:
    print(n%10)
    res += n % 10
    n = n // 10

print(res)