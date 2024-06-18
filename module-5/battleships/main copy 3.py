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

        counter = 1
        for row in self.grid:
            
            display_row = ""
            for cell in row:
                if cell == "S":
                    display_row += "■ "
                elif cell == 'X':
                    display_row += "X "
                else:
                    display_row += "O "
            
            print(f"{counter:2d}   {display_row}")
            # увеличим counter на 1
            counter += 1


class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15

    # Это функция расстановки кораблей, она уже полностью написана
    def place_ships_randomly(self, field, num_ships):
        for _ in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

    # Это функция проверки расстановки кораблей, она уже полностью написана
    def is_valid_ship_placement(self, field, coords, ship_length=1, ):
        x, y = coords

        # Проверка на наличие соседних клеток по горизонтали и вертикали
        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False

        return True

    def play(self):
        
        # Создадим поле игрока и поле компьютера
        self.player_field = Field(self.size, self.ships)
        self.computer_field = Field(self.size, self.ships)



        print("Расстановка кораблей компьютера:")

        print("Ваша расстановка кораблей:")



# Запуск программы
if __name__ == "__main__":
    # создадим игру
    game = BattleshipGame()
    game.play()