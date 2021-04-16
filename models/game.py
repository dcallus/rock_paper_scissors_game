import random

class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.computer = None
        self.big_bang_mode = False

        self.win_game = [["Rock","Scissors"], ["Paper","Rock"], ["Scissors", "Paper"]]
    
    def set_the_winner(self, player):
        self.winner = player

    def return_winner(self):
        return self.winner

    def test_result(self, player_1, player_2):

        if player_1.gesture == player_2.gesture:
            return None

        # first checks if player_1 = game[0], then checks if player_2 = game[0]
        for game in self.win_game:   # example. win_game[0] = ["Rock","Scissors"]
            if [player_1.gesture, player_2.gesture] == game:  # list = ["Rock","Scissors"]
                self.set_the_winner(self.player_1)
                return self.return_winner()
                
            elif [player_2.gesture, player_1.gesture] == game: # list = ["Rock","Scissors"]
                self.set_the_winner(self.player_2)
                return self.return_winner()

    def activate_big_bang_mode(self):
        self.big_bang_mode = True
        self.win_game = [["Rock","Scissors"], ["Paper","Rock"], ["Scissors", "Paper"], ["Lizard", "Spock"],
        ["Spock", "Scissors"], ["Rock", "Lizard"], ["Paper", "Spock"], ["Scissors", "Lizard"], 
        ["Lizard", "Paper"],  ["Spock", "Rock"]]

    def computer_turn(self):
        if self.big_bang_mode == False:
            random_num = random.randint(0, 2)
            # choose between 1 of 3 options
            self.computer = self.win_game[random_num][0]
        
        elif self.big_bang_mode == True:
            # choose between 1 of 5 options, list ordered so each selection is possible only once
            random_num = random.randint(0, 4)
            self.computer = self.win_game[random_num][0]



    