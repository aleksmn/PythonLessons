# Объявляем новую функцию
# с параметром name
def say_hello(name):
    print("Привет", name) 


# Вызов функции
# с аргументом
say_hello("Саша")




# Функция с двумя параметрами
def sum_nums(a, b):
    print(a + b)


print(5, 9)
print(25, 39)
print(53425, 9345)

























def getSum(a=0, b=0):

    return a + b



res = getSum(7, 8) * getSum(10, 42) 


print(res)

print(getSum(234,345))