class Player:

    def __init__(self, name):
        self.action_list1 = []
        self.action_list2 = []
        self.name = name
        self.points = 0

    def receive_result(self, action1, action2):
        self.action_list1.append(action1)
        self.action_list2.append(action2)

    def __str__(self):
        return self.name
