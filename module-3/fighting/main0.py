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


# Инициализация персонажа (создание)

def init_person(name, is_enemy = False):
    class_names = list(classes.keys())

    if is_enemy:
        person = {'класс': random.choice(class_names)}
    else:
        choice = int(input('Введите класс: 1-Воин, 2-Лучник, 3-Маг\n'))
        person = {'класс': class_names[choice-1]}

    person.update({'характеристики': classes[person['класс']]})
    person.update({'имя': name})

    print(f"{person['имя']} - {person['класс']}, имеет характеристики: {person['характеристики']}")
    return person







player = init_person(input('Введите имя игрока: '))
enemy = init_person('Враг', True)