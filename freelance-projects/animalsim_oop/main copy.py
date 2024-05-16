import random

class Tiger:
    def __init__(self):
        self.state = "Выследить добычу"
        self.successful_attack_prob = 0.5
        self.x, self.y = 0, 0

    def update_state(self, rabbits):
        if self.state == "Выследить добычу":
            print("Тигр выслеживает добычу!")
            self.move_randomly()

            # Проверяем, есть ли рядом заяц,
            # если рядом заяц, то меняем state на "Атаковать добычу"
            # ...

        elif self.state == "Атаковать добычу":
            ...


    def move_randomly(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        # делаем границы поля
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

        if self.x > 4:
            self.x = 4
        if self.y > 4:
            self.y = 4



    def __str__(self):
        return f"T (тигр): ({self.x}, {self.y})"
    




class Rabbit:
    def __init__(self):
        self.x = random.randint(1, 4)
        self.y = random.randint(1, 4)
        self.captured = False  # схвачен или нет

    def to_capture(self):
        self.captured = True

    def __str__(self):
        return f"З (заяц): ({self.x}, {self.y})"
    



def print_field(tiger, rabbits=[]):
    field = []
    for _ in range(5):
        row = ["."] * 5
        field.append(row)

    field[tiger.x][tiger.y] = "Т"

    for rabbit in rabbits:
        if not rabbit.captured:
            field[rabbit.x][rabbit.y] = "З"

    for row in field:
        print(" ".join(row))
    print()



# Запуск симуляции
if __name__ == "__main__":

    tiger = Tiger()
    rabbit1 = Rabbit()
    rabbit2 = Rabbit()
    rabbits = [rabbit1, rabbit2]

    while tiger.state != "Бежать домой":
        tiger.move_randomly()

        print_field(tiger, rabbits)
