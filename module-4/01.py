
n = 7
res = 0
for i in range (1, n+1):
    res += i
print(res)



# Рекурсия
def recursion(n):
	if n == 1:
		return 1
	return n + recursion(n - 1)


print(recursion(7))





# def factorial(n):
# 	if n == 0:
# 		return 1
# 	else:
# 		return n * factorial(n - 1)
	

# print(factorial(5))