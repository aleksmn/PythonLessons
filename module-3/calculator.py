from operators import divide_nums

while True:
    choice = input('Введите действие: ')
    if choice in {'+', '-', '*', '/', 'q'}:
        if choice != 'q':
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
            print('Выход из калькулятора')
            break
    else:
        print('Такого действия нет.')
