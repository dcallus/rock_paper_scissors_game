"""Player class, where the value rock, paper or scissors is stored."""
class Player:
    def __init__(self, name):
        self.name = name
        self.gesture = None

    def set_gesture(self, gesture):
        self.gesture = gesture

