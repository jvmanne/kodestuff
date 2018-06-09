from player import Player


class Sequential(Player):

    def __init__(self, number):
        super().__init__("Sequential " + str(number + 1))
        self.turn = -1

    def choose_action(self):
        self.turn = (self.turn + 1) % 3
        return self.turn

    def __str__(self):
        return str(self.name)