# Телефонная книга

import os

os.system('clear')

book_phones = {'Алексей': 23345, 'Дмитрий': 456433, 'Юлия': 3732345}

# print(book_phones)

for k, v in book_phones.items():
    print(k, v)



print("-------------------")
name = input('Имя: ')
phone = input('Телефон: ')



if name and phone:
    book_phones[name] = phone
    for key in book_phones:
        print(f'{key}: {book_phones[key]}' )

elif name and name in book_phones:
    print(book_phones[name])

else:
    print('Нет в телефонной книге')
