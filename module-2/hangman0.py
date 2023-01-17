print("Привет! Я загадал слово, твоя задача угадать его по буквам.")
print("У тебя всего 10 попыток. Удачи!")


word = 'мармелад'


letters = []

hp = 10

while hp > 0:
    for symb in word:
        if symb in letters:
            print(symb, end=' ')
        else:
            print('*', end=' ')
    print()

    user_letter = input("Введите букву: ")
    letters.append(user_letter)

    # Если буквы нет в слове
    if user_letter not in word:
        # вычесть 1 из hp
        hp -= 1
        if hp < 1:
            print("Вы проиграли!")
        else:
            print(f"Осталось попыток: {hp}")

