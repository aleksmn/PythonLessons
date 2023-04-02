white_list = set()
answers = set()


while True:
    white_request = input('Разрешенный запрос:')

    # Если введена пустая строка - выходим из цикла
    if white_request == '':
        break

    # Добавляем строку в белый список
    white_list.add(white_request)



# Проверка белого списка
# print(white_list)


# Ввод запросов от пользователя

while True:
    request = input('Запрос: ')

    if request == '':
        break

    answers.add(request)












# Используем пересечения
# print(white_list & answers)

for a in white_list & answers:
    print(a)
