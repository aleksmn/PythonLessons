import random

# Создать функцию, которая возвращает сумму всех чисел


# Параметры с подсказками типов
# Объявили функцию
def sum_numbers(a: int, b: int) -> int:
    '''
    Функция принимает 2 целых числа и возвращает сумму
    всех натуральных чисел от первого до второго включительно.
    '''
    result = 0

    for i in range(a, b+1):
        result += i

    return result


# print(sum_numbers(7, 12))

# # Вызов функции с аргументами (конкретные значения)
# n = sum_numbers(1, 6) * 2 




def get_random_list(start, end, length):

    rand_list = []

    for i in range(length):
        # получим случайное число
        rand_num = random.randint(start, end)
        rand_list.append(rand_num)

    return rand_list




