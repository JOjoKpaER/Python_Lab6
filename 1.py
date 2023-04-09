class BigBell:

    ringing = ["ding", "dong"]

    def __init__(self):
        self.state = 0

    def sound(self):
        print(self.ringing[self.state])
        self.state = 1 if self.state == 0 else 0


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
