from enum import Enum
import random
from common_func import CommonFunc


TOTAL_FRAME = 10
LAST_FRAME = 9
FULL_SCORE = 10
MIN_MONEY = 15000

class BowlingMenu(Enum):
    """볼링 메뉴 Enum으로 할당"""
    Bowling = 1
    Check_Score = 2
    Home = 3


class Bowling:
    """볼링 클래스 시작"""
    def __init__(self, person):
        self.person = person
        self.money = person.money

        self.rolls = []
        self.scores = []

    def sub_menu(self):
        """Bowling class main_menu"""
        print("볼링치러 왔다.")
        for i in BowlingMenu:
            print("{}. {}".format(i.value, i.name))
        choice = input("입력: ")
        c2 = CommonFunc.values_chk(choice)
        if c2 == BowlingMenu.Bowling.value:
            if self.min_money():
                print("남은 돈: {}".format(self.money))
                input("돈이 부족합니다.")
                self.sub_menu()
            else:
                self.total_score()
        elif c2 == BowlingMenu.Check_Score.value:
            self.show_last_score()
        elif c2 == BowlingMenu.Home.value:
            self.person.go_home()
            self.person.go()
        else:
            print("1~3 사이의 수만 입력하세요.")
            self.sub_menu()

    def pin_maker(self):
        """각 프레임별 점수 생성"""
        for i in range(TOTAL_FRAME):
            pins = []
            for j in range(2):
                input("굴린다아~~~ enter ->")
                if j == 0:
                    pin = random.randint(0, TOTAL_FRAME)
                else:
                    pin = random.randint(0, TOTAL_FRAME-pins[0])
                pins.append(pin)
                print("{}회차 {}번째: {}핀".format((i+1), (j+1), pins[j]))
            self.rolls.append(pins)
            self.show_score(False)

    def total_score(self):
        """점수 계산"""
        if self.rolls:
            self.rolls = []
            self.scores = []

        self.pin_maker()
        score = 0
        roll_index = 0

        for frame in range(TOTAL_FRAME):
            if self.is_strike(roll_index):
                if frame == LAST_FRAME:
                    score += FULL_SCORE
                else:
                    score += FULL_SCORE + self.rolls[roll_index+1][0] + self.rolls[roll_index+1][1]
            elif self.is_spare(roll_index):
                if frame == LAST_FRAME:
                    score += FULL_SCORE
                else:
                    score += FULL_SCORE + self.rolls[roll_index+1][0]
            else:
                score += self.rolls[roll_index][0] + self.rolls[roll_index][1]
            roll_index += 1
            self.scores.append(score)

            if frame == LAST_FRAME:
                self.show_score(True)

        self.money = CommonFunc.left_money(self.money, MIN_MONEY, False)
        print("남은 돈: {}".format(self.money))
        self.again()

    @staticmethod
    def show_frame():
        """스코어 상단표 생성"""
        for l in range(TOTAL_FRAME):
            print("="*10, end='\t')
        print("")

        for m in range(1, 11):
            print("{:^10}".format(m), end='\t')
        print("")

        for n in range(TOTAL_FRAME):
            print("="*10, end='\t')
        print("")

    def show_score(self, is_final):
        """점수 확인"""
        self.show_frame()

        for i in self.rolls:
            if is_final:
                if i[0] == FULL_SCORE:
                    i[0] = "X"
                    i[1] = "-"
                elif i[1] == (FULL_SCORE-i[0]):
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
        """최근 스코어 확인"""
        if not self.rolls:
            input("확인할 점수가 없습니다. 메인으로 enter ->")
            self.sub_menu()
        else:
            self.show_frame()
            for i in self.rolls:
                print("{:^3} | {:^3}".format(i[0], i[1]), end='\t')
            print("")

            for j in self.scores:
                print("{:^10}".format(j), end='\t')
            print("")
            self.again()

    def is_strike(self, roll_index):
        """스트라이크 체크"""
        return self.rolls[roll_index][0] == FULL_SCORE

    def is_spare(self, roll_index):
        """스페어 체크"""
        return self.rolls[roll_index][0] + self.rolls[roll_index][1] == FULL_SCORE

    def again(self):
        """다시하기 메뉴"""
        print("1. 메인으로 2. 집으로")
        choice = input("입력: ")
        c2 = CommonFunc.values_chk(choice)
        if c2 == 1:
            self.sub_menu()
        elif c2 == 2:
            self.person.go_home()
            self.person.go()
        else:
            print("1~2 사이 수만 입력하세요.")
            self.again()

    def min_money(self, min_money=MIN_MONEY):
        """게임 실행시 필요한 최소금액 비교"""
        return self.money < min_money
