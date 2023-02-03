# Телефонная книга


names = ['Квам-Дамн', 'Лук Скамворкер',
         'Петард Вейпер', 'Лия Моргала', 'Эдуард Скамворкер']
phones = ['-79899899889', '112', '1', '+09998765432', '0']


book_phones = {}

for i in range(len(names)):
    book_phones[names[i]] = phones[i]

print(book_phones)
