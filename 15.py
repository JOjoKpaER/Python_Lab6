class NumProg:

    def __init__(self):
        self.commands = self.construct_dict_commands()
        self.numbers = []

    def loop(self):
        cond = True
        while cond:
            cond = self.parse_command(input().split(' '))
        print(*self.numbers)

    def parse_command(self, args):
        if len(args) == 0:
            return False
        if args[0] == 'exit':
            return False
        if len(args) == 1:
            if args[0] in self.commands.keys():
                self.commands[args[0]]()
                return True
        try:
            for i in args:
                self.numbers.append(int(i))
        except:
            return False
        return True

    def construct_dict_commands(self):
        return {
            "make_negative": self.make_negative,
            "square": self.square,
            "strange_command": self.strange_command
        }

    def make_negative(self):
        for i in range(len(self.numbers)):
            if self.numbers[i] > 0:
                self.numbers[i] *= -1

    def square(self):
        for i in range(len(self.numbers)):
            self.numbers[i] **= 2

    def strange_command(self):
        for i in range(len(self.numbers)):
            if self.numbers[i] % 5 == 0:
                self.numbers[i] += 1


prog = NumProg()
prog.loop()
