# Телефонная книга

import os

os.system('clear')

# book_phones = {'Алексей': 23345, 'Дмитрий': 456433, 'Юлия': 3732345}

# Получаем данные из файла

book_phones = {}

with open('book.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
for line in lines:
    line = line.split(';')
    name = line[0].strip()
    phone = line[1].strip()
    book_phones[name] = phone

# print(book_phones)


action = input(
    "Выбери действие: 1 — показать, 2 — добавить, 3 — изменить, 4 — удалить\n")


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
        quit()

    phone = input('Телефон: ')
    book_phones[name] = phone
    print(book_phones)

# Изменение номера
elif action == '3':
    name = input('Имя: ')
    if name not in book_phones:
        print("Контакта нет в книге")
        quit()
    phone = input('Телефон: ')
    book_phones[name] = phone
    print(book_phones)

elif action == '4':
    name = input('Имя для удаления: ')
    if name in book_phones:
        book_phones.pop(name)
        print(book_phones)
    else:
        print("Нет в телефонной книге")


# Переписываем файл

with open('book.txt', 'w', encoding='utf-8') as f:
    for name, number in book_phones.items():
        f.write(f'{name}; {number}\n')
