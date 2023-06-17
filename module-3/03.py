


def sayHello(age, name="Пользователь"):

    print("Привет," , name)
    print("Твой возраст", age)


sayHello(12, "Дима")
sayHello(10)

sayHello(name='Мария', age=14)


# Аргументы переменной длины

def multiply(*args):
  result = 1
  for arg in args:
    result *= arg
  return result



print(multiply(1, 5, 8, 8))













# # Функция map

# new_data = map(int, ['14', '51', '23', '43', '87'])

# new_data = list(new_data)
# print(new_data)   # [14, 51, 23, 43, 87]



# # Использование анонимной функции (lambda)

# new_data = map(lambda a: int(a)**2, ['14', '51', '23', '43', '87'])
# new_data = list(new_data)
# print(new_data)   # [196, 2601, 529, 1849, 7569]
 