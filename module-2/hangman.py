import os
import random
import time


# Очищаем консоль:
os.system('clear || cls')


print('Привет! Я загадал слово, твоя задача - угадать его по буквам.')
print('У тебя 10 попыток')

input("*Нажми Enter, чтобы продолжить*")

string = "мармелад кошка собака береза холодильник образование задача экономика вагон впечатление"

words = string.split()

word = random.choice(words)

letters = []

hp = 10

while hp > 0:
    os.system('clear || cls')

    isWin = True

    for symb in word:
        if symb in letters:
            print(symb, end=" ")

        else:
            print('*', end=" ")
            isWin = False

    print()

    if isWin:
        print('Ты угадал! Молодец!')
        break

    user_letter = input('Введите букву: ')
    letters.append(user_letter)

    if user_letter not in word:
        hp -= 1
        if hp < 1:
            print("Ты проиграл!")
            print("Ответ: ", word)
            break
        else:
            print(f'Осталось попыток: {hp}')
            time.sleep(0.5)

