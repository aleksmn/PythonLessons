import random
import time


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


def apply_skill(enemy: dict) -> None:
    rand = random.randint(0, 9)
    if rand < 4:
        skill = random.choice(list(enemy['характеристики']['навыки'].keys()))
        enemy['характеристики']['защита'] += enemy['характеристики']['навыки'][skill]

        print(f"{enemy['имя']} применяет способность {skill}!")


def attack_enemy(enemy1: dict, enemy2: dict) -> None:
    print(f"{enemy1['имя']} атакует {enemy2['имя']}!")
    time.sleep(2)
    apply_skill(enemy2)
    damage = enemy1['характеристики']['атака'] - enemy2['характеристики']['защита']
    if damage < 0:
        damage = 1
    enemy2['характеристики']['здоровье'] -= damage
    print(f"{enemy1['имя']} наносит {damage} урона и", end=" ")
    if enemy2['характеристики']['здоровье'] <= 0:
        print(f"{enemy2['имя']} потерпел поражение!")
    else:
        print(f"у {enemy2['имя']} остается {enemy2['характеристики']['здоровье']} здоровья!")


def is_valid(text: str, is_role: bool = False) -> bool:

    if len(text.strip()) == 0:
        print('Ошибка ввода. Вы ввели пустую строку.')
        return False

    if is_role:
        if not text.isdigit() or int(text) < 1 or int(text) > len(list(classes.keys())):
            print('Ошибка ввода. Вы ввели неправильный номер класса')
            return False

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
        while True:
            choice = input('Введите класс: 1-Воин, 2-Лучник, 3-Маг\n')
            if is_valid(text=choice, is_role=True):
                break
        person = {'класс': class_names[int(choice)-1]}

    person.update({'характеристики': classes[person['класс']]})
    person.update({'имя': name})

    print(f"{person['имя']} - {person['класс']}, имеет характеристики: {person['характеристики']}")
    return person


# Точка входа в игру
if __name__ == "__main__":
    player = init_person(get_player_name())
    enemy = init_person(get_random_name(), True)

    attack_enemy(player, enemy)