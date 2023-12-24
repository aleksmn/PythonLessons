# Операции над списками

authors = ['Chekhov', 'Dostoevski', 'Tolstoy', 'Nekrasov', 'Bulgakov', 'Pushkin', 'Esenin', 'Blok']

# Изменяем элемент
authors[3] = "Gogol"

# Добавляем элемент
authors.append('Turgenev')

# Удаление
del authors[0]

# Вырезаем элемент
element = authors.pop(3)
print("Удален:", element)

print(authors)


# Получаем индекс элемента
print(authors.index("Tolstoy"))


# Проверка, есть ли элемент в списке
if 'Esenin' in authors:
    print("Есть в списке под индексом", authors.index("Esenin"))
else:
    print("Нет в списке")


# Перебираем список с помощью цикла For
counter = 1
for a in authors:
    print(counter, a)
    counter += 10












# food = ['чебурек', 'огурец', 'сосиска']

# # Можем изменять список
# food[0] = "арбуз"

# print('* Меню на сегодня *')

# # Вывод списка
# counter = 1
# for item in food:
#     print(counter, item)
#     counter += 1


# choice = int(input('Что вы хотите на завтрак? '))


# if choice <= len(food):
#    print(f'Ваша покупка: { food[choice-1] }.\nОтличный выбор!')

# else:
#     print('Нет такого товара')