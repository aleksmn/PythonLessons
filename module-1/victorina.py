print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы:")

questions = [
    "1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?",
    "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?",
    "3. Как называется капитал, который дают инвесторы на развитие стартапа?",
    "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?",
    "5. Какой план создают перед тем, как открывать стартап и занимать деньги?",
    "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?",
    "7. Как называется разница между выручкой и затратами компании?"
]

answers = [
    "Стартап", "Инвестор", "Инвестиция", "MVP", "Бизнес-план", "Конкуренты", "Прибыль"
]


print(questions[0])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[0].lower():
    print("Правильно!")
else:
    print("Неправильно.")