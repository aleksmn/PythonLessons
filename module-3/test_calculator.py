# Операторы

def divide_nums(a, b):
    res = 0
    try:
        res =  float(a) / float(b)
    except ValueError:
        print("Функция работает только с числами.")
    except ZeroDivisionError:
        print("Нельзя делить на ноль.")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        return res

def sum_nums(a, b):
    res = 0
    try:
        res =  float(a) + float(b)
    except ValueError:
        print("Функция работает только с числами.")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        return res

def sub_nums(a, b):
    res = 0
    try:
        res =  float(a) - float(b)
    except ValueError:
        print("Функция работает только с числами.")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        return res

def multiply_nums(a, b):
    res = 0
    try:
        res =  float(a) * float(b)
    except ValueError:
        print("Функция работает только с числами.")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        return res


# Калькулятор

print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n10. Выход')

while True:
    choice = input('Введите номер действия: ')
    if choice in {'1', '2', '3', '4', '10'}:
        if choice != '10':
            num1 = input('Первое число: ')
            num2 = input('Второе число: ')

            if choice == '1':
                print(f'{num1} + {num2} = {sum_nums(num1, num2)}')
            elif choice == '2':
                print(f'{num1} - {num2} = {sub_nums(num1, num2)}')
            elif choice == '3':
                print(f'{num1} * {num2} = {multiply_nums(num1, num2)}')
            elif choice == '4':
                print(f'{num1} / {num2} = {divide_nums(num1, num2)}')
        else:
            print('Выход из калькулятора')
            break
    else:
        print('Такого действия нет.')