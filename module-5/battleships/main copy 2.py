import random


class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships_alive = ships
        self.grid = []

        for i in range(size):
            self.grid.append([None] * 10)


    def display(self, show_ships=False):
        letter_string = "    A B C D E F G H I J"
        print(letter_string)
        # Номер строки
        counter = 1

        for row in self.grid:
            display_row = ""
            for cell in row:
                display_row += "O "

            print(f"{counter:2d}  {display_row}")
            counter += 1





# Запуск программы
if __name__ == "__main__":
    field = Field(10, 15)

    field.display(show_ships=True)