# Калькулятор

num1 = float(input("Первое число: "))
num2 = float(input("Второе число: "))

# выбираем оператор
operation = input("Введите действие (+, -, *, /): ")

if operation == "+":
    print(num1, "+", num2, "=", num1 + num2)

elif operation == "-":
    print(num1, "-", num2, "=", num1 - num2)

elif operation == "*":
    print(num1, "*", num2, "=", num1 * num2)

elif operation == "/":
    print(num1, "/", num2, "=", num1 / num2)

else:
    print("Неправильный ввод")
