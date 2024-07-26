import random


# Генератор случайного математического вопроса
def generate_math_question(a, b):  # a не может быть 0
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operator = random.choice(['+', '-', '*', '/'])

    if operator == "/":
        question = f"{num1*num2} {operator} {num2}"
    else:
        question = f"{num1} {operator} {num2}"
    return question


# Проверка ответа пользователя на правильность
def check_answer(question, user_answer):
    try:
        user_answer = float(user_answer)
        return user_answer == eval(question)
    except ValueError:
        return False


# Проведение теста
def math_quiz(number_of_questions=5):
    correct_answers = 0

    print("Добро пожаловать в математический тест!")

    for i in range(number_of_questions):
        question = generate_math_question(1, 10)
        user_answer = input(f"{question} = ")
        if check_answer(question, user_answer):
            correct_answers += 1

    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if correct_answers >= number_of_questions * 0.8:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers >= number_of_questions * 0.6:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


# Запуск теста
math_quiz(10)