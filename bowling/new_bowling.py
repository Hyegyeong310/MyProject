# new_bowling.py

import random


class Bowing(object):

    def __init__(self):
        self.rolls = []

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
        print(self.rolls)
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

        self.show_score(score)

    def is_strike(self, roll_index):
        return self.rolls[roll_index][0] == 10

    def is_spare(self, roll_index):
        return self.rolls[roll_index][0] + self.rolls[roll_index][1] == 10

    def show_score(self, score):
        pass

a = Bowing()
a.total_score()