items = []

while True:
    item = input("Покупка: ")
    # Выход из цикла, если ввод пустой
    if item == '':
        break
    # Добавляем товар в список покупок
    items.append(item)




print(items)