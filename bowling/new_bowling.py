# new_bowling.py

import random


class Bowing(object):

    def __init__(self):
        self.rolls = []
        self.scores = []

    def pin_maker(self):
        for i in range(10):
            pins = []
            for j in range(2):
                if j == 0:
                    pin = random.randint(0, 10)
                else:
                    pin = random.randint(0, (10-pins[0]))
                pins.append(pin)
            self.roll(pins)

    def roll(self, pins):
        self.rolls.append(pins)

    def total_score(self):
        self.pin_maker()
        score = 0
        roll_index = 0
        for frame in range(10):
            if self.is_strike(roll_index):
                if frame == 9:
                    score += 10
                else:
                    score += 10 + self.rolls[roll_index+1][0] + self.rolls[roll_index+1][1]
            elif self.is_spare(roll_index):
                if frame == 9:
                    score += 10
                else:
                    score += 10 + self.rolls[roll_index+1][0]
            else:
                score += self.rolls[roll_index][0] + self.rolls[roll_index][1]
            roll_index += 1
            self.scores.append(score)

        self.show_score()

    def is_strike(self, roll_index):
        return self.rolls[roll_index][0] == 10

    def is_spare(self, roll_index):
        return self.rolls[roll_index][0] + self.rolls[roll_index][1] == 10

    def show_score(self):
        for l in range(10):
            print("*"*10, end="\t")
        print("")

        for m in range(10):
            print("{:^10}".format(m+1), end="\t")
        print("")

        for n in range(10):
            print("*"*10, end="\t")
        print("")

        for i in self.rolls:
            if i[0] == 10:
                i[0] = "X"
                i[1] = "-"
            elif i[1] == (10-i[0]):
                i[1] = "/"
            elif i[0] == 0:
                i[0] = "-"
            elif i[1] == 0:
                i[1] = "-"

            print("{:^5}|{:^4}".format(i[0], i[1]), end="\t")
        print("\n")

        for j in self.scores:
            print("{:^10}".format(j), end="\t")
        print("")

a = Bowing()
a.total_score()