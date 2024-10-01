from Player import Player
from Enemy import Enemy


class Game:
    def __init__(self):
        self.player = Player()

        self.game_loop()
        

    def adventure_handler(self):
        print(f"{self.player.name} отправился на поиски приключений")


    def shop_handler(self):
        print(f"Ты зашел в волшебный магазин. В твоем кошельке: {self.player.money}" )


    def game_loop(self):
        while self.player.is_alive:
            
            action = input(f"{self.player.name}, выбери действие: \n1 - искать приключения\n2 - пойти в магазин\n3 - выйти из игры\n") 

            if action == "1":
                self.adventure_handler()

            elif action == "2":
                self.shop_handler()

            elif action == "3":
                print(f"{self.player.name} слишком устал от всего этого, поэтому он решил уйти на пенсию.")
                print(f"К тому же, он заработал целых {self.player.money} монет и, возможно, ему хватит этого до конца жизни.")
                print('Выход из игры.')
                break

        print("Вы проиграли!")


if __name__ == "__main__":
    Game()