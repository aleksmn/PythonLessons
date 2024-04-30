import random


class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships_alive = ships
        self.grid = []

        # создаем решетку поля
        for _ in range(size):
            self.grid.append([None] * self.size)    


    def display(self, show_ships=True):
        letter_string = "     A B C D E F G H I J"
        print(letter_string)

        for i, row in enumerate(self.grid):
            
            display_row = ""

            for cell in row:
                if cell == "S":
                    display_row += "■ "
                elif cell == 'X':
                    display_row += "X "
                else:
                    display_row += "O "

            print(f"{(i+1):2d}   {display_row}")





# Запуск программы
if __name__ == "__main__":
    field = Field(10, 15)
    field.display()