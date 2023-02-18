# Пользователь вводит номер телефона в формате:
# 86575432167

# Нужно преобразовать номер телефона в формат:
# +7 (657) 543-21-67

name = input('Введите имя: ')
phone = input("Введите номер телефона (11 цифр): ")
comment = input('Комментарий: ')


phone = f'+7 ({phone[1:4]}) {phone[4:7]}-{phone[7:9]}-{phone[9:]}'


# Создаем контакт
contact = f'{name}; {phone}; {comment}'

print(contact)


# Добавляем контакт в файл

with open('my-contacts.txt', 'a', encoding='utf-8') as f:
    f.write(contact + '\n')



# Все контакты
print("*** Все контакты ***")

with open('my-contacts.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')




