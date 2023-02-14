# Задача 1
# Гласные и согласные
# Напиши программу, которая считает количество гласных
# и согласных букв в слове



# word = input('Введите слово\n')

# g = 'аоуыиэеёюя'
# s = 'бвгджзйклмнпрстфхцчшщ'

# g_count = 0
# s_count = 0

# for letter in word.lower():
#     if letter in g:
#         g_count += 1


# print('Гласные:', g_count)

# print('Согласные:', s_count)









# Задача 2
# Какого цвета клетка?
# Пользователь вводи координату клетки шахматной доски, например a5
# Необходимо определить, какого цвета эта клетка.


# coords_input = input('Write coords, for example a5: \n')

# letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


# try:

#     x = letters[coords_input[0]]
#     y = int(coords_input[1])

# except:
#     print('Неверный ввод')
#     quit()



# print(x, y)

# if (x + y) % 2 == 0:
#     print('Черная клетка')
# else:
#     print('Белая клетка')


# Задача 4
# Написать программу для подсчета
# среднего значения всех введенных пользователем чисел. 
# Индикатором окончания ввода будет служить ввод пустой строки.


# nums = []

# while True:

#     user_input = input('Введите число: ')

#     if user_input == '':
#         break

#     try:
#         user_input = float(user_input)
#         nums.append(user_input)
#     except:
#         pass

    
# print('--------------------')

# if len(nums) > 0:

#     print(nums)

#     avg = sum(nums) / len(nums)

#     print('Среднее значение: ')
#     print(avg)
#     print('Больше среднего значения:')

#     new_nums = [x for x in nums if x > avg]

#     print(new_nums)




# else:
#     print('Неверный ввод')


# Генератор списков

# nums = [3, 6, 8, 0, 1, 2, 4, 5]

# new_nums = [x for x in nums if x > 5]

# print(new_nums)


# Задача 7

# Рассчитаем наибольший общий делитель для двух целых чисел с использованием цикла
# #
# # Запрашиваем у пользователя два целых числа
# n = int(input("Введите первое целое число: "))
# m = int(input("Введите второе целое число: "))

# # Присваиваем d наименьшее из n и m

# d = m if m < n else n

# # В цикле находим наибольший общий делитель для двух чисел
# while n % d != 0 or m % d != 0:
#     d = d - 1
# # Выводим результат
# print("Наибольший общий делитель для", n, "и", m, "равен", d)


# Задача 8
##
# Вывести таблицу умножения от 1 до 10
# #
# MIN = 1
# MAX = 10
# # Строка заголовков
# print("    ", end = "")
# for i in range(MIN, MAX + 1):
#     print(f'{i:4}', end="")
# print()

# # Выводим таблицу
# for i in range(MIN, MAX + 1):
#     print(f'{i:4}', end="")
#     for j in range(MIN, MAX + 1):
#         print(f'{(i * j):4}', end="")
#     print()



# Задача 9


# import random


# results = []

# # Выполняем 20 экспериментов
# for i in range(20):

#     my_list = []

#     while True:
#         my_list.append(random.choice(['O', 'R']))

#         if len(my_list) > 2:
#             if my_list[-1] == my_list[-2] == my_list[-3]:
#                 break


#     print(my_list, 'попыток', len(my_list))

#     results.append(len(my_list))


# # Выводим список, сколько понадобилось попыток, чтобы выбросить 3 одинаковых значения
# print(results)

# print('Среднее значение', sum(results) / len(results))





##
# Создаем колоду карт и перетасовываем ее
#
from random import randrange
## Генерируем стандартную колоду карт с четырьмя мастями и 13 номиналами в каждой
def createDeck():
    # Создаем список для хранения карт
    cards = []
    # Проходим по всем мастям и номиналам
    for suit in ["s", "h", "d", "c"]:
        for value in ["2", "3", "4", "5", "6", "7", "8", "9", \
            "T", "J", "Q", "K", "A"]:
            # Генерируем карту и добавляем ее в колоду
            cards.append(value + suit)
    # Возвращаем целую колоду
    return cards

# print(createDeck())

def shuffle(cards):
    # Проходим по картам
    for i in range(0, len(cards)):
        # Выбираем случайный индекс между текущим индексом и концом списка
        other_pos = randrange(i, len(cards))
        # Меняем местами текущую карту со случайно выбранной
        temp = cards[i]
        cards[i] = cards[other_pos]
        cards[other_pos] = temp


cards = createDeck()

print(cards)

shuffle(cards)

print(cards)