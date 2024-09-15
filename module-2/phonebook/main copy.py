# Телефонная книга

# book_phones = {
#     'Квам-Дамн': '-79899899889',
#     'Лук Скамворкер': '112',
#     'Петард Вейпер': '1',
#     'Лия Моргала': '+09998765432',
#     'Эдуард Скамворкер': '0'
# }


# Получаем данные из файла

book_phones = {}

# открываем файл для чтения
with open("book.txt", "r", encoding="utf-8") as file:
    # читаем файл построчно
    for line in file:
        line = line.split(":")
        name = line[0].strip()
        phone = line[1].strip()
        # Добавляем запись
        book_phones[name] = phone



action = input("Выбери действие: 1 — показать, 2 — добавить, 3 — изменить, 4 — удалить\n")

if action == '1':
    name = input('Имя: ')
    if name in book_phones:
        print(book_phones[name])
    else:
        print("Нет в телефонной книге")


elif action == '2' or action == '3':
    name = input('Имя: ')
    phone = input('Телефон: ')
    # Добавляем запись
    book_phones[name] = phone
    # Вывод телефонной книги
    for name, phone in book_phones.items():
        print(f"{name}: {phone}")

elif action == '4':
    name = input("Имя: ")

    # проверяем, есть ли такое имя
    if name in book_phones:
        # Удаляем
        del book_phones[name]
        # Вывод телефонной книги
        for name, phone in book_phones.items():
            print(f"{name}: {phone}")
    else:
        print("Нет в телефонной книге")


else:
    print('Такого действия нет')


# Сохраним телефонную книгу в файле

# w - перезаписать файл
with open("book.txt", "w", encoding="utf-8") as file:
    for name, phone in book_phones.items():
        file.write(f"{name}: {phone}\n")
