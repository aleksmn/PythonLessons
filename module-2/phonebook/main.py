# Телефонная книга
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

action = input("Выбери действие: 1 — показать, 2 — добавить, 3 — изменить, 4 — удалить\n")

if action == '1':
    name = input('Имя: ')
    if name in book_phones:
        print(book_phones[name])
    else:
        print("Нет в телефонной книге")

# Добавление номера или изменение номера
elif action == '2' or action == "3":
    name = input('Имя: ')
    phone = input('Телефон: ')
    # Добавляем запись
    book_phones[name] = phone
    # Вывод телефонной книги
    for k, v in book_phones.items():
        print(f'{k}: {v}')

# Удаление 
elif action == '4':
    name = input('Имя для удаления: ')
    if name in book_phones:
        # Удаляем
        del book_phones[name]
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
