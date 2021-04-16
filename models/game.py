class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        

        self.win_game = [["Rock","Scissors"], ["Paper","Rock"], ["Scissors", "Paper"]]

        """ big bang mode:
        self.win_game = [["Rock","Scissors"], ["Paper","Rock"], ["Scissors", "Paper"], 
        ["Rock", "Lizard"], ["Lizard", "Spock"], ["Spock", "Scissors"], ["Scissors", "Lizard"], 
        ["Lizard", "Paper"], ["Paper", "Spock"], ["Spock", "Rock"]]
        """
    
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
        self.win_game = [["Rock","Scissors"], ["Paper","Rock"], ["Scissors", "Paper"], 
        ["Rock", "Lizard"], ["Lizard", "Spock"], ["Spock", "Scissors"], ["Scissors", "Lizard"], 
        ["Lizard", "Paper"], ["Paper", "Spock"], ["Spock", "Rock"]]
                

    