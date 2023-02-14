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