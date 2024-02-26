# Создадим функцию деления с обработкой ошибок (исключений)
def divide_nums(a, b):
    result = 0
    try:
        result = float(a) / float(b)
    except ZeroDivisionError:
        print("Ошибка: на ноль делить нельзя")
    except ValueError:
        print("Ошибка: функция работает только с числами")

    return result

# Умножение
def multiply_nums(a, b):
    result = 0
    try:
        result = float(a) * float(b)
    except ValueError:
        print("Ошибка: функция работает только с числами")        
    return result


# Сложение
def sum_nums(a, b):
    result = 0
    try:
        result = float(a) + float(b)
    except ValueError:
        print("Ошибка: функция работает только с числами")        
    return result


# вычитание
def sub_nums(a, b):
    result = 0
    try:
        result = float(a) - float(b)
    except ValueError:
        print("Ошибка: функция работает только с числами")        
    return result

while True:
    choice = input('Введите действие (q - выход): ')
    if choice in ('+', '-', '*', '/', 'q'):

        if choice == 'q':
            print('Выход из калькулятора')
            break

        num1 = input('Первое число: ')
        num2 = input('Второе число: ')

        if choice == '+':
            print(f'{num1} + {num2} = {sum_nums(num1, num2)}')
        elif choice == '-':
            print(f'{num1} - {num2} = {sub_nums(num1, num2)}')
        elif choice == '*':
            print(f'{num1} * {num2} = {multiply_nums(num1, num2)}')
        elif choice == '/':
            print(f'{num1} / {num2} = {divide_nums(num1, num2)}')

    else:
        print('Такого действия нет.')
