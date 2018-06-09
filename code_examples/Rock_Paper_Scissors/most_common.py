from player import Player


class MostCommon(Player):

    def __init__(self, number):
        super().__init__("Most Common " + str(number + 1))

    def choose_action(self):
        if self.action_list2:
            return (max(self.action_list2, key=self.action_list2.count) + 1) % 3
        return 0

    def __str__(self):
        return str(self.name)