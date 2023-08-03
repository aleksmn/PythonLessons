
# # Функция с необязательным аргументом
# def sayHello(age, name="Пользователь"):
#     print("Привет," , name)
#     print("Возраст:", age)


# sayHello(12)
# # Позиционные агрументы
# sayHello(18, "Дима")
# # Именованные аргументы
# sayHello(name="Юлия", age=15)



# # # Аргументы переменной длины

# def multiply(*nums):
#     '''Перемножаем все аргументы'''
#     res = 1
#     for i in nums:
#         res *= i
#     return res



# print(multiply(1, 5, 8, 8, 11))
# print(multiply(1, 5, 8))
# print(multiply(1, 5, 8, 99, 0, 5, 1, 1, 1, 2))






# Аргументы переменной длины в формате ключ=значение

# def create_user(**params):
    
#     return(params)


# print(create_user(fname="Виталий", lname="Иванов", job='Учитель'))





# # Функция map
# Исходные данные (список строк, которые нужно преобразовать с числа)
nums =  ['14', '51', '23', '43', '87']

# Вызываем функцию int для каждого элемента в списке nums
new_data = map(int, nums)

# Получаем список 
new_data = list(new_data)

print(new_data)   # [14, 51, 23, 43, 87]






# Используем свою функцию в функции map
# def get_square(num):
#   return int(num)**2

# new_data = list(map(get_square, nums))
# print(new_data) 



# # Используем анонимную функцию (lambda)

new_data = list(map(lambda num: int(num)**2, nums))
print(new_data) 





# # Фильтруем данные с помощью функции filter

numbers = [-1, -2, 5, 4, -1, 100, 99]

numbers = list(filter(lambda a: a > 0, numbers))

print(numbers)