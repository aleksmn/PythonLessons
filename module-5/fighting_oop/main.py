import random

class Person:
    role = {
        '1': 'Воин',
        '2': 'Лучник',
        '3': 'Маг',
    }

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

    def __init__(self, name, is_enemy):
        self.name = name
        self.is_enemy = is_enemy
        self.person_class = self.get_person_class()
        self.person_class_dict = self.classes[self.person_class]
        self.health = self.person_class_dict['здоровье']
        self.attack = self.person_class_dict['атака']
        self.defence = self.person_class_dict['защита']
        self.money = 1000.0
        self.skills = self.person_class_dict['навыки']
        self.inventory = ['яблоко', 'шаурма']
        self.is_alive = True

        print(f"{self.name} - {self.person_class}.")
        print("У него такие характеристики:")
        print(f" здоровье - {self.health},\n атака - {self.attack},\n защита - {self.defence}.")


    def get_person_class(self):
        if self.is_enemy:
            random_choice = random.choice(list(self.role.keys()))
            # random_choice = random.choice('123')
            return self.role[random_choice]
        else:
            choice = input(f"Введите роль: 1-Воин, 2-Лучник, 3-Маг\n")
            return self.role[choice]


player = Person('Олег', is_enemy=False)
ogr = Person('Комочек тьмы', is_enemy=True)


# print(player.name)