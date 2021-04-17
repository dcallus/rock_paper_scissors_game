import random
from models.player import Player

class Game:
    def __init__(self, player_1, player_2=None):
        self.player_1 = player_1
        self.player_2 = player_2
        self.big_bang_mode = False

        self.win_game = [["Rock","Scissors"], ["Paper","Rock"], ["Scissors", "Paper"]]
    
    def set_the_winner(self, player):
        self.winner = player

    def test_result(self, player_1, player_2):
        if player_1.gesture == player_2.gesture:
            return None

        # first checks if player_1 = game[0], then checks if player_2 = game[0]
        for game in self.win_game:
            if [player_1.gesture, player_2.gesture] == game: 
                self.set_the_winner(self.player_1)
                break
                
            elif [player_2.gesture, player_1.gesture] == game:
                self.set_the_winner(self.player_2)
                break

        return self.winner

    def activate_big_bang_mode(self):
        self.big_bang_mode = True
        self.win_game = [["Rock","Scissors"], ["Paper","Rock"], ["Scissors", "Paper"], ["Lizard", "Spock"],
        ["Spock", "Scissors"], ["Rock", "Lizard"], ["Paper", "Spock"], ["Scissors", "Lizard"], 
        ["Lizard", "Paper"],  ["Spock", "Rock"]]

    def _set_computer_gesture(self):
        if self.big_bang_mode == False:
            self.player_2 = random.choice(["Rock", "Paper", "Scissors"])
        
        elif self.big_bang_mode == True:
            self.player_2 = random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])
    
    def create_computer_player(self):
        self.player_2 = Player("Computer")
        self._set_computer_gesture()