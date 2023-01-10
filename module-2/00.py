food = [ 'чебурек', 'огурец', 'сосиска']

print('* Меню на сегодня *')

for counter, item in enumerate(food):
    print(counter+1, item)



choice = int(input('Что вы хотите на завтрак? '))




if choice <= len(food):
    print(f'Ваша покупка: { food[choice-1] }!')

else:
    print('Нет такого товара')