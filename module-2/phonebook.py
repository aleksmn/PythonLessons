book_phones = {
    'Квам-Дамн': '-79899899889',
    'Лук Скамворкер': '112',
    'Петард Вейпер': '1',
    'Лия Моргала': '+09998765432',
    'Эдуард Скамворкер': '0'
}



while True:

    action = input("Выбери действие: 1 — показать, 2 — добавить, 3 — изменить, 4 — удалить\n")

    if action == "":
        print("Спасибо за использование нашей программы!")
        break

    elif action == '1':
        name = input("Имя: ")

        if name in book_phones:
            print(book_phones[name])

        else:
            print("Нет в телефонной книге")

    # Добавить контакт
    elif action == "2":
        # спрашиваем новое имя и новый номер телефона
        name = input('Имя: ')
        phone = input('Телефон: ')
        # Добавляем запись
        book_phones[name] = phone
        # Вывод телефонной книги
        for k, v in book_phones.items():
            print(k, v)

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

    elif action == "5":
        # только имена
        for name in book_phones:
            print(name)

    elif action == "6":
        # только номера
        for k, v in book_phones.items():
            print(v)




# сохраним в текстовом файле
# w - write - открыть файл для записи
with open("book.txt", "w", encoding="utf-8") as file:
    for k, v in book_phones.items():
        file.write(f'{k}: {v}\n')
    