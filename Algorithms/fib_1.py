import timeit

# Числа Фибоначчи

n = 25

def fib0(n):
    f1, f2 = 0, 1
    for i in range(n-1):
        f1, f2 = f2, f1 + f2

    return f2


# Рекурсия
def fib1(n):
    return n if n <= 1 else fib1(n-1) + fib1(n-2)

reps = 100


print('fib0:', timeit.timeit(lambda: fib0(n), number=reps))
print('fib1:', timeit.timeit(lambda: fib1(n), number=reps))