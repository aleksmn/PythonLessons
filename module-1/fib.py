# # 1 1 2 3 5 8 13 21

n = int(input("Введите число: "))

fib1 = 1
fib2 = 1

while fib1 <= n:
    print(fib1)
    temp = fib1
    fib1 = fib2
    fib2 = temp + fib2

print(fib1)



