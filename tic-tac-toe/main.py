# Поле для игры
board = list(range(1, 10))

# Счетчик ходов
counter = 0

# Флажок выигрыша
is_win = False

# Условия победы
win_coords = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)


# Объявим функцию для отрисовки доски
def draw_board():
    print("Игра Крестики-нолики")
    
    for i in range(3):
        print("-" * 13)
        print(f"| {board[0 + 3 * i]} | {board[1 + 3 * i]} | {board[2 + 3 * i]} |")

    print("-" * 13)



while not is_win:

    draw_board()

    if counter % 2 == 0:
        player_token = "X"
    else:
        player_token = "O"


    player_answer = input(f'Куда ставим {player_token}?: ')

    # Делаем поправку на -1
    player_answer = int(player_answer) - 1

    # Делаем ход
    board[player_answer] = player_token
    counter += 1











# def draw_board():
#     print("Игра Крестики-нолики")

#     for i in range(3):

#         print('-' * 13)
#         print(
#             f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')

#     print('-' * 13 + "\n")





# # Игровой цикл

# while not is_win:

#     draw_board()

#     if counter % 2 == 0:
#         player_token = 'X'
#     else:
#         player_token = 'O'

#     player_answer = input(f'Куда ставим {player_token}?: ')

#     # Получаем ход от игрока, делаем поправку "-1" для учета индексации с 0.
#     player_answer = int(player_answer) - 1


#     if str(board[player_answer]) not in 'XO':
#         board[player_answer] = player_token
#     else:
#         print('Эта ячейка уже занята!')
#         continue

#     # Увеличиваем ход на 1
#     counter += 1

#     # Проверяем на выигрыш
#     if counter > 4:
#         for each in win_coords:
#             # Проверяем наличие выигрышной комбинации (для X или O)
#             if board[each[0]] == board[each[1]] == board[each[2]]:
#                 is_win = True
#                 break

#         if is_win:
#             draw_board()
#             print(f'* Победил {player_token}!  Поздравляем! *\n')
#             break

#     # Проверяем на ничью
#     if counter == 9:
#         draw_board()
#         print('Победила дружба :)\n')
#         break
