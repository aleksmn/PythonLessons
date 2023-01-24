import random

print("*** Магическая Восьмерка ***")

name = input('Введите свое имя: ')

while True:

    question = input('Введите вопрос: ')

    if question == '':
        break

    random_number = random.randint(1, 9)

    if random_number == 1:
        answer = "Определенно, да"
    elif random_number == 2:
        answer = "Решительно, да"
    elif random_number == 3:
        answer = "Без сомнений"
    elif random_number == 4:
        answer = "Ответ неясный, попробуй еще раз"
    elif random_number == 5:
        answer = "Попробуй еще раз, позже"
    elif random_number == 6:
        answer = "Лучше тебе не говорить сейчас"
    elif random_number == 7:
        answer = "Мои источники говорят, что нет"
    elif random_number == 8:
        answer = "Перспектива не очень"
    elif random_number == 9:
        answer = "Очень сомнительно"

    else:
        answer = "Ошибка"


    # Выдаем ответ

    print(name + ' справшивает: ' + question)

    print('Ответ магической 8-ки: ' + answer)
