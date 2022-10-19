board = list(range(1, 10))

# print(board)

# Параметры поля
cells = 3
dashes = 13
spaces = 4

# Счетчик ходов
counter = 0

is_win = False

# Условия попеды
win_coords = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)


def draw_board():
    '''Отрисовка поля в консоли'''

    for i in range(3):
        shift = i * 3
        print(spaces * ' ', end="")
        print('-' * dashes)
        print(spaces * ' ', end="")
        print(
            f'| {board[0 + shift]} | {board[1 + shift]} | {board[2 + shift]} |')

    print(spaces * ' ', end="")
    print('-' * dashes + "\n")


print("\n* Игра Крестики-нолики *\n")


# Игровой цикл

while not is_win:

    draw_board()

    if counter % 2 == 0:
        player_token = 'X'
    else:
        player_token = 'O'

    player_answer = input(f'Куда ставим {player_token}?: ')

    # Получаем ход от игрока, делаем поправку "-1" для учета индексации с 0.
    player_answer = int(player_answer) - 1

    if str(board[player_answer]) not in 'XO':
        board[player_answer] = player_token
    else:
        print('Эта ячейка уже занята!')
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
            print(f'* Победил {player_token}!  Поздравляем! *\n')
            break

    if counter == 9:
        draw_board()
        print('Победила дружба :)\n')
        break
