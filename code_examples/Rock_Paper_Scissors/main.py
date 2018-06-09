from game import *
from random_player import RandomPlayer
from sequential import Sequential
from most_common import MostCommon
from historian import Historian
from input_player import  InputPlayer
import matplotlib.pyplot as plt


def main0():
    players, rounds = [input("Player 1: "), input("Player 2: ")], int(input("Rounds: "))
    print()
    for x in range(2):
        if players[x].lower() == "r":
            players[x] = RandomPlayer(x)
        elif players[x].lower() == "s":
            players[x] = Sequential(x)
        elif players[x].lower() == "m":
            players[x] = MostCommon(x)
        elif players[x].lower() == "h":
            players[x] = Historian(x)
        else:
            name = players[x]
            players[x] = InputPlayer()
            players[x].name = name

    games = Games(players[0], players[1], rounds)
    return games.play_tournament()

def main():
    plt.figure()
    results = main0()
    plt.plot(results, "-k")
    plt.show()

if __name__ == "__main__":
    main()