import random

min_number = 0
max_number = 255

attempt = 0 # Количество попыток
input_number = 0 # Число, которое вводит пользователь

def start_game():
    # attempt = 0 # Количество попыток
    # input_number = 0 # Число, которое вводит пользователь
    print(f'Я загадал число от {min_number} до {max_number}')

    # Локальное пространство имен
    # print(locals())


def game_loop():
    case = random.randint(min_number, max_number) # Загадываем число

    global input_number
    global attempt

    while input_number != case:
        input_number = int(input("Угадай число: "))
        attempt += 1

        if input_number < case:
            print('Твое число слишком маленькое!')
        elif input_number > case:
            print('Твое число слишком большое!')
        else:
            print('Угадал!')


def end_game():
    print(f'Ты сделал попыток {attempt}.')



start_game()
game_loop()
end_game()

# Встроенное пространство имен:
# print(dir(__builtins__))

# Глобальное пространство имен:
# print(globals())


