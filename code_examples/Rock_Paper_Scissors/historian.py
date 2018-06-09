from player import Player


class Historian(Player):
    def __init__(self, number, remember = 3):
        super().__init__("Historian " + str(number + 1))
        self.remember = remember

    def choose_action(self):
        if self.action_list2:
            last_actions = self.action_list2[-self.remember:]
            next_actions = []
            for i in range(len(self.action_list2[:-self.remember])):
                if last_actions == self.action_list2[i:i + self.remember]:
                    next_actions.append(self.action_list2[i + self.remember])
            if next_actions:
                return (max(next_actions, key=next_actions.count) + 1) % 3
        return 0

    def __str__(self):
        return str(self.name)