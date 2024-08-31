import random


class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships_alive = ships   # количество кораблей
        self.grid = []   # поле для игры


