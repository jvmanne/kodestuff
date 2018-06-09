from player import Player
from random import randint


class RandomPlayer(Player):

    def __init__(self, number):
        super().__init__("Random " + str(number + 1))

    def choose_action(self):
        return randint(0,2)

    def __str__(self):
        return str(self.name)