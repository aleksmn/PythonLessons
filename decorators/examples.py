# Определение декоратора
def uppercase_decorator(function):
    def wrapper():
        # Вызов функции и получение результата
        result = function()
        # Преобразование результата в верхний регистр
        result = result.upper()
        # Возврат преобразованного результата
        return result
    # Возвращение обернутой функции
    return wrapper

# Применение декоратора к функции
@uppercase_decorator
def say_hello():
    return 'Привет, мир!'

# Вызов декорированной функции
print(say_hello())




import time

def timer_decorator(function):
    def wrapper():
        start_time = time.time()
        result = function()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции: {execution_time} секунд")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    return "Завершено"

slow_function()



def check_args_decorator(function):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Аргументы должны быть целыми числами")
        return function(*args, **kwargs)
    return wrapper

@check_args_decorator
def sum_numbers(a, b):
    return a + b

sum_numbers(2, 3)    # Вернет 5
sum_numbers(2.5, 3)  # Вызовет исключение TypeError