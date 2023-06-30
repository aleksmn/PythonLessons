
# Методы списка

authors = ['Chekhov', 'Dostoevski', 'Tolstoy', 'Nekrasov', 'Bulgakov', 'Pushkin', 'Esenin', 'Blok']

# Изменяем элемент
authors[3] = "Gogol"

# Добавляем элемент
authors.append('Turgenev')

# Вырезаем элемент
element = authors.pop(1)
print("Удален:", element)

# Удаление
del authors[0]

# Получаем индекс элемента
print(authors.index("Tolstoy"))

for a in authors:
    print(a)












food = ['чебурек', 'огурец', 'сосиска']

# Можем изменять список
food[0] = "арбуз"

print('* Меню на сегодня *')

# Вывод списка
counter = 1
for item in food:
    print(counter, item)
    counter += 1


choice = int(input('Что вы хотите на завтрак? '))


if choice <= len(food):
   print(f'Ваша покупка: { food[choice-1] }.\nОтличный выбор!')

else:
    print('Нет такого товара')