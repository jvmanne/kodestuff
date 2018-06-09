import matplotlib.pyplot as plt
from random_player import RandomPlayer


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.actions = ["Rock", "Paper", "Scissors"]
        self.action1 = 0
        self.action2 = 0
        self.win = ""

    def play_game(self):
        self.action1 = self.player1.choose_action()
        self.action2 = self.player2.choose_action()

        if self.action1 == self.action2:
            self.win = "No one"
        elif self.action2 - self.action1 == 1 or self.action1 - self.action2 == 2:
            self.win = str(self.player2)
            self.player2.points += 1
        else:
            self.win = str(self.player1)
            self.player1.points += 1

        self.player1.receive_result(self.action1, self.action2)
        self.player2.receive_result(self.action2, self.action1)


    def __str__(self):
        s = str(self.player1) + ": " + self.actions[self.action1] + "\n"
        s += str(self.player2) + ": " + self.actions[self.action2] + "\n"*2
        return s + str(self.win) + " has won the game"


class Games:
    def __init__(self, player1, player2, number_of_games):
        self.number_of_games = number_of_games
        self.player1 = player1
        self.player2 = player2

    def play_game(self):
        game = Game(self.player1, self.player2)
        game.play_game()
        print(game)

    def play_tournament(self):
        results = []
        for x in range(self.number_of_games):
            print("Round", x+1)
            self.play_game()
            result = "Points:\n\t"
            result += str(self.player1) + ": " + str(self.player1.points) + "\n\t"
            result += str(self.player2) + ": " + str(self.player2.points) + "\n"*2
            results.append(self.player1.points/(x+1))
            print(result)
        if self.player1.points > self.player2.points:
            print(str(self.player1), "has won the tournament")
        elif self.player1.points < self.player2.points:
            print(str(self.player2), "has won the tournament")
        else:
            print("No one has won the tournament")
        return results