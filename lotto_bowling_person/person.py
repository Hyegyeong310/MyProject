# person.py

from enum import Enum
from common_func import CommonFunc
from home import Home
from lotto import Lotto
from bowling import Bowling


LOTTO_MIN = 5000
BOWLING_MIN = 15000

class MainMenu(Enum):
    HOME = 1
    LOTTO = 2
    BOWLING = 3


class Person:

    def __init__(self, money):
        self.common = CommonFunc()
        self.money = self.common.values_chk(money)
        self.place = None

    def sub_menu(self):
        print("무엇을 할까~~")
        for i in MainMenu:
            print("{}. {}".format(i.value, i.name), end='\t')
        print("")

        choice = input("입력: ")
        c2 = self.common.values_chk(choice)
        if c2 == MainMenu.HOME.value:
            self.go_home()
        elif c2 == MainMenu.LOTTO.value:
            if self.min_money(LOTTO_MIN):
                input("돈 없어. 집에 가자 enter ->")
                self.go_home()
            else:
                self.go_lotto()
        elif c2 == MainMenu.BOWLING.value:
            if self.min_money(BOWLING_MIN):
                input("돈 없어. 집에 가자 enter ->")
                self.go_home()
            else:
                self.go_bowling()
        else:
            input("1~3 중 선택하세요 enter ->")
            return self.sub_menu()

        self.go()

    def min_money(self, min_money):
        return self.money < min_money

    def go(self):
        if self.place:
            self.place.sub_menu()
        else:
            print("Error!")

    def go_home(self):
        self.place = Home(self)

    def go_lotto(self):
        self.place = Lotto(self)

    def go_bowling(self):
        self.place = Bowling(self)
