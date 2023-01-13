# Словарь (dict)


my_dictionary = {
    'один': 'one',
    'два': 'two',
    'три': 'three'
}


# print(type(my_dictionary))

my_dictionary['четыре'] = 'four'


while True:
    w = input('Слово на русском: ')
    t = input('Слово на английском: ')

    if w == '' or t == '':
        break

    my_dictionary[w] = t


# print(my_dictionary)


for k, v in my_dictionary.items():
    print(k, v)


user_input = input('Какое слово найти? ')

if user_input in my_dictionary:
    print('Перевод: ', my_dictionary[user_input])

else:
    print('Нет в словаре')
