
"""

Задача 1: Декоратор для проверки авторизации пользователя

Напишите декоратор login_required, который проверяет, 
авторизован ли пользователь. Если пользователь авторизован, 
то функция выполняется, иначе выводится сообщение об ошибке.

"""
"""
def login_required(function):
    def wrapper(is_logged_in):
        if is_logged_in:
            return function()
        else:
            print("Ошибка: Вы не авторизованы")
    return wrapper

@login_required
def protected_function():
    print("Выполняется защищенная функция")

protected_function(is_logged_in=True)    # Выполнится
protected_function(is_logged_in=False)   # Выведет сообщение об ошибке


"""





"""
Задача 2: Декоратор для логирования

Напишите декоратор logger, который записывает логи выполнения функции в файл.

"""
"""

def logger(function):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as file:
            file.write(f"Выполняется функция {function.__name__}\n")
        return function(*args, **kwargs)
    return wrapper

@logger
def add_numbers(a, b):
    return a + b

add_numbers(2, 3)    # Добавит запись в log.txt о выполнении функции add_numbers
"""

"""

Задача 3: Декоратор для кэширования

Напишите декоратор cache, который кэширует результаты выполнения 
функции и возвращает их при повторном вызове функции с теми же аргументами.

"""
"""
def cache(function):
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = function(*args)
            cache_dict[args] = result
            return result

    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))    # Вернет значение из кэша
print(fibonacci(10))   # Вернет вычисленное значение и добавит его в кэш

"""