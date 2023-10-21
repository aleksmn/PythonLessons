def divide_nums(a,b):
    res = 0 
    try:
        res = float(a) / float(b)
    except ValueError:
        print("Функция деления работает только с числами.")
    except ZeroDivisionError:
        print("Нельзя делить на ноль.")
    except Exception as e:
        print("Ошибка:",e)
    finally:
        return f"{a} / {b} = {res}"




def sum_nums(a,b):
    res = 0 
    try:
        res = float(a) + float(b)
    except ValueError:
        print("Функция сложения работает только с числами.")
    
    except Exception as e:
        print("Ошибка:",e)
    finally:
        return f"{a} + {b} = {res}"
    


def sub_nums(a,b):
    res = 0 
    try:
        res = float(a) - float(b)
    except ValueError:
        print("Функция вычитания работает только с числами.")
    
    except Exception as e:
        print("Ошибка:",e)
    finally:
        return f"{a} - {b} = {res}"
    


def multiply_nums(a,b):
    res = 0 
    try:
        res = float(a) * float(b)
        
    except ValueError:
        print("Функция умножения работает только с числами.")
    
    except Exception as e:
        print("Ошибка:",e)
    finally:
        return f"{a} * {b} = {res}"
    


print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n10. Выход')
while True:
    choice = input('Введите номер действия: ')
    if choice == "1" or choice == "2" or choice == "3"or choice == "4":
        a = (input("Введите первое число: "))
        b = (input("Введите второе число: "))
    if choice in ["1","2","3","4","10"]:
        if choice == "1":
            print(sum_nums(a,b))
        elif choice == "2":
            print(sub_nums(a,b))
        elif choice == "3":
            print(multiply_nums(a,b))
        elif choice == "4":
            print(divide_nums(a,b))
        elif choice == "10":
            print('Выход из калькулятора')
            break
    else:
        print("Такого действия нет.")