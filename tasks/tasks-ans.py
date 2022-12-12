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


coords_input = input('Write coords, for example a5: \n')

letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


try:

    x = letters[coords_input[0]]
    y = int(coords_input[1])

except:
    print('Неверный ввод')
    quit()



print(x, y)

if (x + y) % 2 == 0:
    print('Черная клетка')
else:
    print('Белая клетка')

