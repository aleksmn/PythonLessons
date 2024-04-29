import random


class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships_alive = ships
        self.grid = []

        # создаем пустую сетку
        for _ in range(size):
            self.grid.append([None] * size)





# Запуск программы
if __name__ == "__main__":
    field = Field(10, 15)

    print(field.grid)