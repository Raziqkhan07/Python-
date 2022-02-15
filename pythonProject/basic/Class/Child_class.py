class Player:

    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

    def play(self):
        print("Player {} starts running".format(self.name))

class Goalkeeper(Player):

    def __init__(self, name, role):
        super().__init__(name, 'football')
        self.role = role

class Defender(Player):

    def __init__(self, name, role):
        super().__init__(name, 'football')
        self.role = role

class Midfielder(Player):

    def __init__(self, name, role):
        super().__init__(name, 'football')
        self.role = role

class Striker(Player):

    def __init__(self, name, role):
        super().__init__(name, 'football')
        self.role = role
    midfielder1 = Midfielder('James Midfielder', 'midfielder')
    midfielder1.play()