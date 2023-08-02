
# # Функция с необязательным аргументом
# def sayHello(age, name="Пользователь"):

#     print("Привет," , name)
#     print("Возраст:", age)


# # sayHello(21)
# # sayHello(18, name="Дима")
# # # Именованные аргументы
# # sayHello(age=10, name="Дима")
# # # Позиционные аргументы
# # sayHello(22)



# # sayHello(name='Мария', age=14)


# # # Аргументы переменной длины

# def multiply(*args):
#   result = 1
#   for arg in args:
#     result *= arg
#   return result



# print(multiply(1, 5, 8, 8, 11))













# # Функция map
# Исходные данные (список строк, которые нужно преобразовать с числа)
nums =  ['14', '51', '23', '43', '87']

new_data = list(map(int, nums))

print(new_data)   # [14, 51, 23, 43, 87]


# Используем свою функцию в функции map
# def get_square(num):
#   return int(num)**2

# new_data = list(map(get_square, nums))
# print(new_data) 



# Используем анонимную функцию (lambda)

new_data = list(map(lambda a: int(a)**2, nums))
print(new_data) 



# Фильтруем данные с помощью функции filter

numbers = [-1, -2, 5, 4, -1, 100, 99]

numbers = list(filter(lambda a: a > 0, numbers))

print(numbers)