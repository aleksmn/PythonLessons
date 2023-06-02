from Player import Player
from Enemy import Enemy



if __name__ == "__main__":

    player = Player()

    enemy = Enemy()

    player.fight_for_the_win(player, enemy)