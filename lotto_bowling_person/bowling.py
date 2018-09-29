from enum import Enum
import random
import home


class BowlingMenu(Enum):
    볼링치기 = 1
    점수확인 = 2
    집으로 = 3


class Bowling(object):
    def __init__(self, money):
        self.money = money
        self.rolls = []
        self.scores = []
        self.place = None

    def sub_menu(self):
        print("볼링치러 왔다.")
        for i in BowlingMenu:
            print("{}. {}".format(i.value, i.name))
        choice = input("입력: ")
        c2 = self.values_chk(choice)
        if c2 == BowlingMenu.볼링치기.value:
            if self.min_money():
                print("남은 돈: {}".format(self.money))
                input("돈이 부족합니다.")
                return self.sub_menu()
            else:
                return self.total_score()
        elif c2 == BowlingMenu.점수확인.value:
            return self.show_last_score()
        elif c2 == BowlingMenu.집으로.value:
            self.place = Home(self.money)
            self.place.sub_menu()
        else:
            print("1~3 사이의 수만 입력하세요.")
            return self.sub_menu()

    def pin_maker(self):
        for i in range(10):
            pins = []
            for j in range(2):
                input("굴린다아~~~ enter ->")
                if j == 0:
                    pin = random.randint(0, 10)
                else:
                    pin = random.randint(0, 10-pins[0])
                pins.append(pin)
                print("{}회차 {}번째: {}핀".format((i+1), (j+1), pins[j]))
            self.rolls.append(pins)
            self.show_score(False)

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

            if frame == 9:
                self.show_score(True)

        self.left_money(15000)
        self.again()

    def show_score(self, is_final):

        for l in range(10):
            print("="*10, end='\t')
        print("")

        for m in range(1, 11):
            print("{:^10}".format(m), end='\t')
        print("")

        for n in range(10):
            print("="*10, end='\t')
        print("")

        for i in self.rolls:
            if is_final:
                if i[0] == 10:
                    i[0] = "X"
                    i[1] = "-"
                elif i[1] == (10-i[0]):
                    i[1] = "/"
                elif i[0] == 0:
                    i[0] = "-"
                elif i[1] == 0:
                    i[1] = "-"
            print("{:^3} | {:^3}".format(i[0], i[1]), end='\t')
        print("")

        for j in self.scores:
            print("{:^10}".format(j), end='\t')
        print("")

    def show_last_score(self):
        if len(self.rolls) == 0:
            input("확인할 점수가 없습니다. 메인으로 enter ->")
            self.sub_menu()
        else:
            for l in range(10):
                print("=" * 10, end='\t')
            print("")

            for m in range(1, 11):
                print("{:^10}".format(m), end='\t')
            print("")

            for n in range(10):
                print("=" * 10, end='\t')
            print("")

            for i in self.rolls:
                print("{:^3} | {:^3}".format(i[0], i[1]), end='\t')
            print("")

            for j in self.scores:
                print("{:^10}".format(j), end='\t')
            print("")
            self.again()

    def is_strike(self, roll_index):
        return self.rolls[roll_index][0] == 10

    def is_spare(self, roll_index):
        return self.rolls[roll_index][0] + self.rolls[roll_index][1] == 10

    def again(self):
        print("1. 메인으로 2. 집으로")
        choice = input("입력: ")
        c2 = self.values_chk(choice)
        if c2 == 1:
            return self.sub_menu()
        elif c2 == 2:
            self.place = Home(self.money)
            return self.place.sub_menu()
        else:
            print("1~2 사이 수만 입력하세요.")
            return self.again()

    def min_money(self, min_money=15000):
        return self.money < min_money

    def left_money(self, newMoney):
        self.money = self.money - newMoney
        print("남은 돈: {}".format(self.money))

    def values_chk(self, str):
        while True:
            try:
                num = int(str)
                return num
            except:
                str = input("숫자만 입력해주세요: ")
                return self.values_chk(str)