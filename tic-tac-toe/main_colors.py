import colorama
import os


# Объявляем цвета

colorama.init()
green = colorama.Fore.GREEN
red = colorama.Fore.RED
blue = colorama.Fore.BLUE
reset = colorama.Fore.RESET

board = list(range(1, 10))

# print(board)

# Параметры поля
cells = 3
dashes = 13
spaces = 4

# Счетчик ходов
counter = 0

is_win = False

# Условия победы
win_coords = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

# Список токенов игроков
tokens_list = [red + 'X' + reset, green + 'O' + reset]



def draw_board():
    '''Отрисовка поля в консоли'''

    os.system('cls')

    print(green + "\n* Игра Крестики-нолики *\n" + reset)
    for i in range(3):
        shift = i * 3
        print(spaces * ' ', end="")
        print('-' * dashes)
        print(spaces * ' ', end="")
        print(
            f'| {board[0 + shift]} | {board[1 + shift]} | {board[2 + shift]} |')

    print(spaces * ' ', end="")
    print('-' * dashes + "\n")



# Игровой цикл

while not is_win:

    draw_board()

    player_token = tokens_list[counter % 2]

    player_answer = input(f'{reset}Куда ставим {player_token}?: ')

    # Выполняем валидацию (проверку) ввода
    if not player_answer.isdigit():
        print("Ошибка ввода. Можно вводить только числа")
        input("Нажмите Enter")
        continue

    if not 0 < int(player_answer) < 10:
        print("Ошибка ввода. Введите число от 1 до 9")
        input("Нажмите Enter")
        continue     


    # Делаем поправку "-1" для учета индексации с 0.
    player_answer = int(player_answer) - 1


    if str(board[player_answer]) not in tokens_list:
        board[player_answer] = player_token
    else:
        print(f'{red}Эта ячейка уже занята{reset}')
        input("Нажмите Enter")
        continue

    counter += 1

    if counter > 4:
        for each in win_coords:
            # Проверяем наличие выигрышной комбинации (для X или O)
            if board[each[0]] == board[each[1]] == board[each[2]]:
                is_win = True
                break

        if is_win:
            draw_board()
            print(blue + f'* Победил {player_token + blue}!  Поздравляем! *\n')
            break

    if counter == 9:
        draw_board()
        print(blue + 'Победила дружба :)\n')
        break
