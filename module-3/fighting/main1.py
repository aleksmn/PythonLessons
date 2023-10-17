import random

role = {'1': 'Воин', '2': 'Лучник', '3': 'Маг'}


classes = {

    'Воин': {
        'здоровье': 100,
        'атака': 30,
        'защита': 25,
        'навыки': {
            'щит': 10
        }
    },

    'Лучник': {
        'здоровье': 50,
        'атака': 40,
        'защита': 20,
        'навыки': {
            'убежать': 10
        }
    },

    'Маг': {
        'здоровье': 30,
        'атака': 50,
        'защита': 15,
        'навыки': {
            'магический щит': 10,
            'лечение': 10
        }
    }
}



# Валидация

def is_valid(text: str, is_role: bool = False) -> bool:

    # Проверка на пустую строку
    if len(text.strip()) == 0:
        print('Ошибка ввода. Вы ввели пустую строку.')
        return False
    
    elif text not in role and is_role == True:
        print('Ошибка ввода. Вы ввели неправильное значение. Введите числа от 1 до 3.')
        return False
    
    else:
        return True



def get_random_name() -> str:

    first_names = [
        'Доктор', 'Летающий', 'Профессор', 'Скучный',
        'Мега', 'Железный', 'Голодный', 'Капитан',
        'Быстрый', 'Мистер', 'Горячий', 'Звездный',
        'Космический', 'Просто', 'Восхитительный', 'Непобедимый'
    ]

    second_names = [
        'слесарь', 'мухомор', 'пепел', 'лемур',
        'шаман', 'пельмень', 'слизень', 'алхимик',
        'крот', 'фикус', 'кролик', 'танцор',
        'пингвин', 'викинг', 'паук', 'плащ'
    ]

    return f"{random.choice(first_names)} {random.choice(second_names)}"


def get_player_name() -> str:
    while True:
        player_name = input(f'Как зовут твоего героя?\n')
        if is_valid(player_name):
            break
    return player_name







# Инициализация персонажа (создание)

def init_person(name: str, is_enemy: bool = False):
    class_names = list(classes.keys())
    if is_enemy:
        person = {'класс': random.choice(class_names)}
    else:
        choice = input('Введите класс: 1-Воин, 2-Лучник, 3-Маг\n')
        person = {'класс': class_names[int(choice)-1]}

    person.update({'характеристики': classes[person['класс']]})
    person.update({'имя': name})

    print(f"{person['имя']} - {person['класс']}, имеет характеристики: {person['характеристики']}")
    return person


# Точка входа в игру
if __name__ == "__main__":
    player = init_person(get_player_name())
    enemy = init_person(get_random_name(), True)