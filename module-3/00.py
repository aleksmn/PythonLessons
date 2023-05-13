
# Объявляем новую функцию
# с параметром name

def sayHello(name):
    print("Привет ", name) 


# Вызов функции
# с аргументом
sayHello("Михаил")






def getSum(a=0, b=0):

    return a + b



res = getSum(7, 8) * getSum(10, 42) 


print(res)

print(getSum(234,345))