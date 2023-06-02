from Player import Player
from Enemy import Enemy


def main():

    player = Player()
    enemy = Enemy()

    player.fight_for_the_win(player, enemy)



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Выход из игры...")
        quit()
