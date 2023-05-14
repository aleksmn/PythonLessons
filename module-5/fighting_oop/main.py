# Пример решения задания
class Person:
    classes = {
        'Воин': {
            'здоровье': 100,
            'атака': 50,
            'защита': 25,
            'навыки': {
                'щит': 20
            }
        },
        'Лучник': {
            'здоровье': 70,
            'атака': 80,
            'защита': 15,
            'навыки': {
                'убежать': 10
            }
        },
        'Маг': {
            'здоровье': 50,
            'атака': 90,
            'защита': 15,
            'навыки': {
                'магический щит': 45,
                'лечение': 20
            }
        }
    }

    def __init__(self, name, person_class, is_enemy):
        self.name = name
        self.person_class = self.classes[person_class]
        self.health = self.person_class['здоровье']
        self.attack = self.person_class['атака']
        self.defence = self.person_class['защита']
        self.money = 1000.0
        self.skills = self.person_class['навыки']
        self.inventory = ['яблоко', 'шаурма']
        self.is_alive = True
        self.is_enemy = is_enemy


player = Person(name='Вася', person_class='Воин', is_enemy=False)
enemy = Person(name='Летающий чугун', person_class='Лучник', is_enemy=True)


print(player.name)