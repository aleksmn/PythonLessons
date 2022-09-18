# s = "81005557889"

# # +7 (100) 555-78-89

# formated = f'+7 ({s[1:4]}) {s[4:7]}-{s[7:9]}-{s[9:]}'


# print(formated)


# Калькулятор


# num1 = input("Первое число: ")
# num2 = input("Второе число: ")


# try:
#     num1 = float(num1)
#     num2 = float(num2)
# except:
#     print("Неверный ввод")
#     quit()

# # выбираем оператор
# operation = input("Введите действие (+, -, *, /): ")

# if operation == "+":
#     print(num1, "+", num2, "=", num1 + num2)

# elif operation == "-":
#     print(num1, "-", num2, "=", num1 - num2)

# elif operation == "*":
#     print(num1, "*", num2, "=", num1 * num2)

# elif operation == "/":
#     print(num1, "/", num2, "=", num1 / num2)

# else:
#     print("Неправильный ввод")


# input()


# Проверка пароля

# p = "11111111"


# if len(p) < 8:
#     print("Очень слабый пароль")

# elif p.isnumeric() == False and p.isalpha() == False and p.islower() == False and p.isupper() == False:
#     print("Хороший!")

# elif p.isalpha() == False and p.isnumeric() == False:
#     print("Средний")

# elif p.isalpha() == True or p.isnumeric() == True:
#     print('Слабый')
