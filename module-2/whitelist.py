white_list = set()
user_requests = set()


while True:
    white_request = input('Разрешенный запрос:')

    # Если введена пустая строка - выходим из цикла
    if white_request == '':
        break

    # Добавляем строку в белый список
    white_list.add(white_request)



# Проверка белого списка
print(white_list)


# Ввод запросов от пользователя

while True:
    request = input('Запрос: ')

    if request == '':
        break

    user_requests.add(request)



# Используем пересечения
# print(white_list &  user_requests)

for a in white_list & user_requests:
    print(a)
