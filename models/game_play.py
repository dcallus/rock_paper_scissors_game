from models.game import *
from models.player import *



def get_results(player_1_gesture, player_2_gesture):
    player_1 = Player('Player 1', player_1_gesture)
    player_2 = Player('Player 2', player_2_gesture)

    game_play = Game(player_1, player_2)  # create new game instance
    result = game_play.test_result(player_1, player_2)  # test winner + return result
    return result