import random


class Field:
    def __init__(self, size, ships):
        self.size = size
        self.grid = []
        for _ in range(size):
            self.grid.append([None] * size)
        self.ships_alive = ships

    def display_lines(self, show_ships=False):
        # Возвращает список строк
        lines = []

        letter_string = "    A B C D E F G H I J"
        lines.append(letter_string)
        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                if cell == "S" and show_ships:
                    display_row += "■ "
                elif cell == 'X':
                    display_row += "X "
                else:
                    display_row += "O "

            # Выводим строку поля
            lines.append(f"{(i+1):2d}  {display_row}")
        return lines

class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15

        self.player_field = Field(self.size, self.ships)
        self.computer_field = Field(self.size, self.ships)

    def place_ships_randomly(self, field, num_ships):
        for _ in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1),
                          random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

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
    
    def player_turn(self):
        x = input("Введите координату выстрела x: ")
        y = int(input("Введите координату выстрела y: "))

        x = "ABCDEFGHIJ".index(x.upper())
        y -= 1

        if self.computer_field.grid[y][x] == "S":
            print("Вы попали!")
            self.computer_field.grid[y][x] = "X"
            self.computer_field.ships_alive -= 1
        else:
            print("Промах!")


    def computer_turn(self):
        x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        if self.player_field.grid[y][x] == "S":
            print("Компьютер попал!")
            self.player_field.grid[y][x] = "X"
            self.player_field.ships_alive -= 1
        else:
            print("Компьютер промахнулся!")

    # Начало игры
    def play(self):
        self.place_ships_randomly(self.computer_field, self.ships)
        self.place_ships_randomly(self.player_field, self.ships)

        print("Ваша расстановка кораблей:", "\t", "Расстановка кораблей компьютера:")

        while True:
            player_lines = self.player_field.display_lines(show_ships=True)
            comp_lines = self.computer_field.display_lines(show_ships=True)
            for i in range(self.size + 1):
                print(player_lines[i], "\t", comp_lines[i])

            self.player_turn()
            if self.computer_field.ships_alive == 0:
                print("Вы победили! Все корабли компьютера потоплены.")
                break

            self.computer_turn()
            if self.player_field.ships_alive == 0:
                print("Вы проиграли! Все ваши корабли потоплены.")
                break


# Запуск программы
if __name__ == "__main__":

    game = BattleshipGame()
    game.play()
