# # Словарь (dict)


my_dictionary = {
    'один': 'one',
    'два': 'two',
    'три': 'three'
}

print(my_dictionary['один'])
print(my_dictionary['два'])
print(my_dictionary['три'])

# Изменение записи
my_dictionary['один'] = '1'

# Добавление записи
my_dictionary['четыре'] = 'four'


# Удаление
del my_dictionary['один']


print("Вывод словаря")

for rus, eng in my_dictionary.items():
    print(f'Слово: {rus}, перевод: {eng}')




















# print(my_dictionary['один'])
# print(my_dictionary['два'])

# my_dictionary['четыре'] = 'four'


# print(type(my_dictionary))




# while True:
#     w = input('Слово на русском: ')
#     t = input('Слово на английском: ')

#     if w == '' or t == '':
#         break

#     my_dictionary[w] = t


# # print(my_dictionary)


# for k, v in my_dictionary.items():
#     print(k, v)


# user_input = input('Какое слово найти? ')

# if user_input in my_dictionary:
#     print('Перевод: ', my_dictionary[user_input])

# else:
#     print('Нет в словаре')




# Телефонная книга
# Создаем словарь из двух списков:

# names = ['Квам-Дамн', 'Лук Скамворкер', 'Петард Вейпер', 'Лия Моргала', 'Эдуард Скамворкер']
# phones = ['-79899899889', '112', '1', '+09998765432', '0']


# book_phones = {}

# counter = 0

# for name in names:
#     book_phones[name] = phones[counter]
#     counter += 1


# print(book_phones)






# book_phones = {
#     'Квам-Дамн': '-79899899889',
#     'Лук Скамворкер': '112',
#     'Петард Вейпер': '1',
#     'Лия Моргала': '+09998765432',
#     'Эдуард Скамворкер': '0',
# }


# name = input("Имя: ")

# number = input("Номер телефона: ")


# if name and number:
#     # Добавляем или изменяем запись
#     book_phones[name] = number
#     # Выводим 
#     for key in book_phones:
#         print(f'{key}: {book_phones[key]}')

# elif name in book_phones:
#     print(book_phones[name])

# else:
#     print('Нет в телефонной книге')




