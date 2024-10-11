
def check(check_list):

    new_list = []

    for i in check_list:
        if len(i) > 5:
            new_list.append(i)

    return new_list




name_list = []

while True:
    name = input("Введите имя: ")
    if name == "":
        break
    else:
        # Добавляем имя в список
        name_list.append(name)



# Выводим результат
print(check(name_list))
