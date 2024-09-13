import random

from Person import Person
from Constants import role



class Player(Person):
    def __init__(self):
        super().__init__()
        self.set_name()
        self.set_person_class()
        self.set_class_properties()

        self.money = random.randint(10, 500)

        print(f"{self.name} - {self.person_class}.")
        print("У него такие характеристики:")
        print(f" здоровье - {self.health},\n атака - {self.attack},\n защита - {self.defence}, \nденьги - {self.money}")

    def set_name(self):

        player_name = input(f'Как зовут твоего героя?\n')
        self.name = player_name

    def set_person_class(self):
        choice = input(f"Введи роль: 1-Воин, 2-Лучник, 3-Маг\n")
        self.person_class = role[choice]

    def increase_money(self, value):
        self.money += value
        print(f"Заработано {value} руб. Осталось: {round(self.money, 2)} руб.")

    def decrease_money(self, value):
        if self.money - value < 0:
            print(f"Герой не может себе этого позволить. (˘･_･˘)")
            return False
        else:
            self.money -= value
            print(f"Потрачено {value} руб. Осталось: {self.money} руб.")
            return True
        