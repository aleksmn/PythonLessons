from operators import sum_nums, sub_nums, multiply_nums, divide_nums

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
