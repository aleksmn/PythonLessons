from Player import Player
from Enemy import Enemy


class Game:
    def __init__(self):
        self.player = Player()


        self.game_loop()
        

    def adventure_handler(self):
        print(f"{self.player.name} отправился на поиски приключений")
        self.enemy = Enemy()
        self.player.fight_for_the_win(self.player, self.enemy)

        if not self.enemy.is_alive:
            money = self.enemy.attack // 2
            self.player.money += money
            print(f"{self.player.name} победил и заработал {money}. Теперь у него {self.player.money}")


    def shop_handler(self):

        print(f"Ты зашел в волшебный магазин. В твоем кошельке: {self.player.money}" )
        print(f"Твои текущие характеристики: здоровье {self.player.health}, атака {self.player.attack}, защита {self.player.defence}.")

        choice = input(f"{self.player.name}, выбери действие: \
                        \n1 - восстановить здоровье за 50 монет\n2 - защите +10 за 100 монет\n3 - атака +5 за 200 монет\n4 - выйти\n")
        
        if choice == "1":
            if self.player.decrease_money(50):
                self.player.health = self.player.max_health
                print("Твое здоровье:", self.player.health)

        elif choice == "2":
            if self.player.decrease_money(100):
                self.player.defence += 10
                print("Твоя защита теперь:", self.player.defence)            

        elif choice == "3":
            if self.player.decrease_money(200):
                self.player.attack += 5
                print("Твоя атака теперь:", self.player.attack)

        elif choice == "4":
            print("Вы вышли из магазина")

        else:
            print("Действие не распознано")


    def game_loop(self):
        while self.player.is_alive:
            
            action = input(f"{self.player.name}, выбери действие: \n1 - искать приключения\n2 - пойти в магазин\n3 - выйти из игры\n") 

            if action == "1":
                self.adventure_handler()

            elif action == "2":
                self.shop_handler()

            elif action == "3":
                print(f"{self.player.name} слишком устал для всего этого, поэтому он решил уйти на пенсию.")
                print(f"К тому же, он заработал целых {self.player.money} монет и, возможно, ему хватит этого до конца жизни.")
                print('Выход из игры.')

        print("Вы проиграли!")


if __name__ == "__main__":
    try:
        Game()
    except KeyboardInterrupt:
        print("Выход из игры...")
        quit()
