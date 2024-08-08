import random

class Tiger:
    def __init__(self):
        self.state = "Выследить добычу"
        self.successful_attack_prob = 0.5
        self.x, self.y = 0, 0








def print_field():
    field = []
    for i in range(5):
        row = ["."] * 5
        field.append(row)

    # Выводим поле на экран
    for row in field:
        print(" ".join(row))
    
    print() # пустая строка



# Точка входа в программу
if __name__ == "__main__":
    # Объект тигр
    tiger = Tiger()


    # Игровое поле
    print_field()


