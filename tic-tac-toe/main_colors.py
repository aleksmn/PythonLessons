import colorama
import os
import time


# Объявляем цвета

colorama.init()
white = colorama.Fore.CYAN
green = colorama.Fore.GREEN
red = colorama.Fore.RED
blue = colorama.Fore.BLUE



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





def draw_board():
    '''Отрисовка поля в консоли'''

    os.system('cls||clear')

    print(green + "\n* Игра Крестики-нолики *\n"+blue)
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

    if counter % 2 == 0:
        player_token = 'X'
    else:
        player_token = 'O'

    player_answer = input(f'{white}Куда ставим {player_token}?: ')

    # Получаем ход от игрока, делаем поправку "-1" для учета индексации с 0.
    try:
        player_answer = int(player_answer) - 1
    except:
        print(red + 'Неверный ввод')
        time.sleep(0.6)
        continue

    if str(board[player_answer]) not in 'XO':
        board[player_answer] = player_token
    else:
        print(red + 'Эта ячейка уже занята!' + white)
        time.sleep(0.6)
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
            print(blue + f'* Победил {player_token}!  Поздравляем! *\n')
            break

    if counter == 9:
        draw_board()
        print(blue + 'Победила дружба :)\n')
        break
