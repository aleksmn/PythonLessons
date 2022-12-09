# Игра "Замок дракона"
import time
import random

print("Ты в темной комнате в загадочном замке.")

print("Перед тобой три двери. Ты должен выбрать одну.")

playerChoice = input("Твой выбор: 1, 2 или 3...\n")

time.sleep(1)

if playerChoice == '1':
    print('ВЫБОР 1')

elif playerChoice == '2':
    print('ВЫБОР 2')
    rand = random.randint(1,6)
    print('Перед тобой старинный сундук')
    time.sleep(1)
    print('Твое случайное число:', rand)
    if rand > 4:
        print('Сундук с сокровищами')
    else:
        print('Сундук со змеями!')

elif playerChoice == '3':
    print('ВЫБОР 3')

    dragonChoice = input('Второй выбор действия (1 или 2)\n')

    time.sleep(1)

    if dragonChoice == '1':
        print('Второй выбор - 1')

    elif dragonChoice == '2':
        print('Второй выбор - 2')

    else:
        print('Неверный ввод (второй выбор)')


else:
    print('Неверный ввод')


