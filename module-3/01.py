

username = 'User'

# Глобальная переменная
res = 0

def summa(a, b):
    # Глобальная переменная доступна для чтения внутри функции
    print(username)

    #username = 'Василий'  # ошибка, для изменения переменная не доступна

    # Локальная переменная
    example = 6

    # Изменяем глобальную переменную внутри функции
    global res
    res = a + b

    print(locals())
    print(globals())
    # Глобальное пространство имен
    print(dir(__builtins__))
    


summa(5, 8)

print(res)







# Создай функцию multiply_range(start, end), которая перемножает все целые числа от значения "start" до значения "end" включительно.

# Если значение start больше, чем end, то они меняются местами.



def multiply_range(start:int, end:int) -> int:
    '''Перемножаем числа от start до end'''

    if start > end:
        start, end = end, start

    res = 1
    # Перемножение
    for i in range(start, end+1):
        res *= i

    return res



# Вызов функции
print(multiply_range(10, 5))

