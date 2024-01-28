print("Привет! Я загадал слово, твоя задача угадать его по буквам.")
print("У тебя всего 10 попыток. Удачи!")


word = 'мармелад'


letters = []

hp = 10

while hp > 0:
    # Ставим флажок
    is_win = True

    for symb in word:
        if symb in letters:
            print(symb, end=' ')
        else:
            # Роняем флажок
            is_win = False
            print('*', end=' ')

    # Проверяем флажок
    if is_win:
        print("\nМолодец! Слово отгадано!")
        break

    user_letter = input("\nВведите букву: ")
    letters.append(user_letter)

    # Если буквы нет в слове
    if user_letter not in word:
        # вычесть 1 из hp
        hp -= 1
        if hp < 1:
            print("Вы проиграли! Было загадано слово", word)
        else:
            print(f"Осталось попыток: {hp}")

