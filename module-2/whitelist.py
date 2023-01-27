white_list = set()
answers = set()

white_request = 1
request = 1

while white_request:
    white_request = input('Разрешенный запрос:')
    if white_request:
        white_list.add(white_request)

while request:
    request = input('Запрос: ')
    if request:
        answers.add(request)


# Используем пересечения
# print(white_list & answers)

for a in white_list & answers:
    print(a)
