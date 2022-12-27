import os
import random


# Очищаем консоль:
# os.system('cls')
os.system('clear')



print('Привет! Я загадал слово, твоя задача - угадать его по буквам.')

input("*Нажми Enter, чтобы продолжить*")

words = ['коала', 'пирожок', 'чебурек', 'огурец', 'сосиска', 'котик',
         'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']

word = random.choice(words)


letters = []

hp = 10

while hp > 0:
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
            break
        else:
            print(f'Осталось попыток: {hp}')



