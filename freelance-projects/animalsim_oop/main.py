import random
import time
import os

os.system("cls")

class Tiger:
    def __init__(self):
        self.state = "Выследить добычу"
        self.successful_attack_prob = 0.5
        self.x, self.y = 0, 0

    def update_state(self, rabbits):
        if self.state == "Выследить добычу":
            print("Тигр выслеживает добычу!")
            self.move_randomly()
            if any(self.is_near_rabbit(rabbit) for rabbit in rabbits):
                self.state = "Атаковать добычу"
        elif self.state == "Атаковать добычу":
            if random.random() < self.successful_attack_prob:
                print("Тигр успешно атаковал зайца!")

                for rabbit in rabbits:
                    if self.is_near_rabbit(rabbit):
                        rabbit.to_capture()

                self.state = "Бежать домой"
            else:
                print("Тигр промахнулся!")
        elif self.state == "Бежать домой":
            self.x, self.y = 0, 0

    def move_randomly(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.x = max(0, min(self.x, 4))
        self.y = max(0, min(self.y, 4))

    def is_near_rabbit(self, rabbit):
        return abs(self.x - rabbit.x) <= 1 and abs(self.y - rabbit.y) <= 1




class Rabbit:
    def __init__(self):
        self.x = random.randint(1, 4)
        self.y = random.randint(1, 4)
        self.captured = False  # схвачен или нет

    def to_capture(self):
        self.captured = True


def print_field(tiger, rabbits=[]):
    field = []
    for i in range(5):
        row = ["."] * 5
        field.append(row)

    field[tiger.x][tiger.y] = "Т"

    for rabbit in rabbits:
        if not rabbit.captured:
            field[rabbit.x][rabbit.y] = "З"

    # Выводим поле на экран
    for row in field:
        print(" ".join(row))
    
    print() # пустая строка



# Точка входа в программу
if __name__ == "__main__":
    # Объект тигр
    tiger = Tiger()
    rabbit1 = Rabbit()
    rabbit2 = Rabbit()
    rabbits = [rabbit1, rabbit2]

    while tiger.state != "Бежать домой":

        tiger.update_state(rabbits)
        print_field(tiger, rabbits)

        time.sleep(1)
        os.system("cls")


    if tiger.state == "Бежать домой":
        print("Тигр вернулся домой.")

    tiger.update_state(rabbits)
    print_field(tiger, rabbits)
