# Телефонная книга

# import os

# os.system('clear')

# book_phones = {'Алексей': 23345, 'Дмитрий': 456433, 'Юлия': 3732345}

# Получаем данные из файла

# book_phones = {}

# with open('book.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()

# for line in lines:
#     line = line.split(';')
#     name = line[0].strip()
#     phone = line[1].strip()
#     book_phones[name] = phone

# print(book_phones)

book_phones = {
    'Квам-Дамн': '-79899899889',
    'Лук Скамворкер': '112',
    'Петард Вейпер': '1',
    'Лия Моргала': '+09998765432',
    'Эдуард Скамворкер': '0'
}


action = input(
    "Выбери действие: 1 — показать, 2 — добавить, 3 — изменить, 4 — удалить,  5 — Показать все имена в книге, 6 — Показать все номера в книге \n")


if action == '1':
    name = input('Имя: ')
    if name in book_phones:
        print(book_phones[name])
    else:
        print("Нет в телефонной книге")

# Добавление номера
elif action == '2':
    name = input('Имя: ')

    if name in book_phones:
        print("Контакт существует")
    else:
        phone = input('Телефон: ')
        book_phones[name] = phone
        # Вывод телефонной книги
        for k, v in book_phones.items():
            print(f'{k}: {v}')

# Изменение номера
elif action == '3':
    name = input('Имя: ')
    if name not in book_phones:
        print("Контакта нет в книге")
    else:
        phone = input('Телефон: ')
        book_phones[name] = phone

        # Вывод телефонной книги
        for k, v in book_phones.items():
            print(f'{k}: {v}')


elif action == '4':
    name = input('Имя для удаления: ')
    if name in book_phones:
        book_phones.pop(name)
        # Вывод телефонной книги
        for k, v in book_phones.items():
            print(f'{k}: {v}')
    else:
        print("Нет в телефонной книге")


elif action == '5':
    print('Список имен')
    # Выводим все ключи словаря
    for name, phone in book_phones.items():
        print(name)
    

elif action == '6':
    print('Список номеров')
    for name, phone in book_phones.items():
        print(phone)


else:
    print('Такого действия нет')









# Переписываем файл

# with open('book.txt', 'w', encoding='utf-8') as f:
#     for name, number in book_phones.items():
#         f.write(f'{name}; {number}\n')
