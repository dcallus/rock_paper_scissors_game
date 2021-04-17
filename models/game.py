import random

class Game:
    def __init__(self, player_1, player_2=None, vs_computer_mode=False):
        self.player_1 = player_1
        self.player_2 = player_2
        self.computer = None
        self.big_bang_mode = False

        self.win_game = [["Rock","Scissors"], ["Paper","Rock"], ["Scissors", "Paper"]]
    
    def set_the_winner(self, player):
        self.winner = player

    def return_winner(self):
        return self.winner

    def _test_result(self, player_1, player_2):
        if player_1.gesture == player_2.gesture:
            return None

        # first checks if player_1 = game[0], then checks if player_2 = game[0]
        for game in self.win_game:
            if [player_1.gesture, player_2.gesture] == game: 
                self.set_the_winner(self.player_1)
                return self.return_winner()
                
            elif [player_2.gesture, player_1.gesture] == game:
                self.set_the_winner(self.player_2)
                return self.return_winner()

    def test_result(self, player_1, player_2):
        if vs_computer_mode:


    def activate_big_bang_mode(self):
        self.big_bang_mode = True
        self.win_game = [["Rock","Scissors"], ["Paper","Rock"], ["Scissors", "Paper"], ["Lizard", "Spock"],
        ["Spock", "Scissors"], ["Rock", "Lizard"], ["Paper", "Spock"], ["Scissors", "Lizard"], 
        ["Lizard", "Paper"],  ["Spock", "Rock"]]

    def set_computer_gesture(self):
        """activates computer and gives it a gesture."""

        if self.big_bang_mode == False:
            self.computer = random.choice("Rock", "Paper", "Scissors")
        
        elif self.big_bang_mode == True:
            # each choice has two chances of being returned (not dependent on list order)
            self.computer = random.choice("Rock", "Paper", "Scissors", "Lizard", "Spock")