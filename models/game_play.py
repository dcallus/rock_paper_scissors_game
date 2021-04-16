from models.game import *
from models.player import *


player_1 = Player('Player 1')
player_2 = Player('Player 2')
game_play = Game(player_1, player_2)

def get_results(player_1, player_2):

    result = game_play.test_result(player_1, player_2)  # test winner + return result
    return result