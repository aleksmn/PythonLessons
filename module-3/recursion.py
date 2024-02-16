# Сумма всех чисел до n включительно 
n = 7
res = 0
for i in range (1, n+1):
    res += i
print(res)

# 1 + 2 + 3 + 4 + 5 + 6 + 7



# Рекурсия

def sum_range(n):
	if n == 1:
		return 1
    # рекурсия - вызов функцией самой себя
	return n + sum_range(n - 1)


print(sum_range(7))








def recursion(n):
    print(n)
	
    if n == 1:
        return
    
    return recursion(n - 1)



recursion(7)












































# def factorial(n):
# 	if n == 0:
# 		return 1
# 	else:
# 		return n * factorial(n - 1)
	

# print(factorial(5))


# Число Фибоначчи
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)



# def recursion(n):
#     print(n)
#     if n == 1: 
#       return 1
#     return recursion(n-1)


# recursion(int(input("Введите число: ")))