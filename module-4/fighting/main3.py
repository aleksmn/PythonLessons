import random
import time
import os

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


def is_valid(text: str, is_role: bool = False) -> bool:
    if len(text) == 0:
        print('Ошибка ввода. Вы ввели пустую строку.')
        return False
    elif text not in '123' and is_role == True:
        print('Ошибка ввода. Вы ввели не правильное значение. Введите числа от 1 до 3.')
        return False
    else:
        return True


def get_player_name() -> str:
    while True:
        player_name = input(f'Как зовут твоего героя?\n')
        if is_valid(player_name):
            break
    return player_name


def get_random_name() -> str:
    from random import choice

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

    return f"{choice(first_names)} {choice(second_names)}"



def clear():
    return os.system('clear')


def enter_to_continue():
    input('Нажмите Enter, чтобы продолжить.')


# Инициализация персонажа (создание)

def init_person(name: str, is_enemy: bool = False) -> dict:
    if is_enemy:
        person = {'класс': role[random.choice(list(role.keys()))]}
    else:
        while True:
            choice = input('Введите класс: 1-Воин, 2-Лучник, 3-Маг\n')
            if is_valid(text=choice, is_role=True):
                break
        person = {'класс': role[choice]}

    person.update({'характеристики': classes[person['класс']]})
    person.update({'имя': name})

    print(
        f"{person['имя']} - {person['класс']}, имеет характеристики: {person['характеристики']}")
    return person


def apply_skill(enemy):
    rand = random.randint(0, 9)
    if rand > 6:
        skill = random.choice(list(enemy['характеристики']['навыки'].keys()))
        enemy['характеристики']['здоровье'] += enemy['характеристики']['навыки'][skill]

        print(
            f"{enemy['имя']} применяет способность {skill}!")



def attack_enemy(enemy1: dict, enemy2: dict) -> None:


    print(f"{enemy1['имя']} атакует {enemy2['имя']}!")

    time.sleep(2)

    apply_skill(enemy2)

    damage = enemy1['характеристики']['атака'] - \
        enemy2['характеристики']['защита']
    if damage < 0:
        damage = 1

    enemy2['характеристики']['здоровье'] -= damage
    print(f"{enemy1['имя']} наносит {damage} урона и у {enemy2['имя']} остается {enemy2['характеристики']['здоровье']} здоровья!")



def fight(attacker: dict, defender:dict) -> bool:
    while True:
        time.sleep(2)
        clear()

        if attacker['характеристики']['здоровье'] > 0:
            attack_enemy(attacker, defender)
        else:
            print(f"{attacker['имя']} потерпел поражение!")
            return False
        
        if defender['характеристики']['здоровье'] > 0:
            attack_enemy(defender, attacker)
        else:
            print(f"{defender['имя']} потерпел поражение!")
            return True
    
        enter_to_continue()





clear()

player = init_person(get_player_name())
enemy = init_person(get_random_name(), is_enemy=True)

enter_to_continue()
clear()

# attack_enemy(player, enemy)

fight(player, enemy)
