import random

from Person import Person
from Constants import role


class Enemy(Person):
    def __init__(self):
        super().__init__()
        self.set_name()
        self.person_class = random.choice(list(role.values()))
        self.set_class_properties()

    def set_name(self):
        first_names = ['Доктор', 'Летающий', 'Профессор', 'Скучный', 'Мега', 'Железный', 'Голодный',
                       'Капитан', 'Быстрый', 'Мистер', 'Горячий', 'Звездный', 'Космический', 'Просто', 'Восхитительный',
                       'Непобедимый']
        second_names = ['слесарь', 'мухомор', 'лемур', 'шаман', 'пельмень', 'слизень',
                        'алхимик', 'крот', 'фикус', 'господин', 'кролик', 'танцор', 'пингвин', 'викинг', 'паук', 'плащ']
        self.name = f"{random.choice(first_names)} {random.choice(second_names)}"
