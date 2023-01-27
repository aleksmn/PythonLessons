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

for answer in answers:
  if answer in white_list:
      print(answer)
