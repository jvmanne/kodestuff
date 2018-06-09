from player import Player


class InputPlayer(Player):

    def __init__(self, number = None):
        super().__init__(number)

    def choose_action(self):
        result = input("Rock Paper Scissors: ")
        if (result == "0" or result.lower() == "rock"):
            return 0
        elif (result == "1" or result.lower() == "paper"):
            return 1
        elif (result == "2" or result.lower() == "scissors"):
            return 2
        return 0

    def __str__(self):
        return self.name