# print("Форматируем номер телефона")

# number = input("Введите номер телефона: ")

# username = input("Введите имя: ")

# # # +7 (912) 345-67-89

# # new_number = "+7 (" + number[1:4] + ") " + number[4:7] + "-" + number[7:9] + "-" + number[9:]

# new_number = f'+7 ({number[1:4]}) {number[4:7]}-{number[7:9]}-{number[9:]}'

# print(username, new_number)




# with open("mynumbers.txt", "a", encoding="utf-8") as f:
#     f.write(username + " : " + new_number + "\n")













# s = "81005557889"

# # +7 (100) 555-78-89

# formated = f'+7 ({s[1:4]}) {s[4:7]}-{s[7:9]}-{s[9:]}'


# print(formated)


# Калькулятор


# num1 = input("Первое число: ")
# num2 = input("Второе число: ")

# # выбираем оператор
# operation = input("Введите действие (+, -, *, /): ")

# try:
#     num1 = float(num1)
#     num2 = float(num2)

# except:
#     print("Неверный ввод")
#     quit()


# if operation == "+":
#     print(f'{num1} + {num2} = {num1 + num2}')

# elif operation == "-":
#     print(f'{num1} - {num2} = {num1 - num2}')

# elif operation == "*":
#     print(f'{num1} * {num2} = {num1 * num2}')

# elif operation == "/":
#     print(f'{num1} / {num2} = {num1 / num2}')

# else:
#     print("Неправильный ввод")



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
