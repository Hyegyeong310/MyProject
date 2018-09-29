# person.py

from enum import Enum
import home
import lotto
import bowling


class MainMenu(Enum):
    집으로 = 1
    로또사러 = 2
    볼링치러 = 3


class MinMoneys(Enum):
    lotto_min = 5000
    bowling_min = 15000


class Person(object):
    def __init__(self, money):
        self.money = self.values_chk(money)
        self.place = None

    def sub_menu(self):
        print("무엇을 할까~~")
        for i in MainMenu:
            print("{}. {} 간다.".format(i.value, i.name), end='\t')
        print("")

        choice = input("입력: ")
        c2 = self.values_chk(choice)
        if c2 == MainMenu.집으로.value:
            self.go_home()
        elif c2 == MainMenu.로또사러.value:
            if self.min_money(MinMoneys.lotto_min.value):
                input("돈 없어. 집에 가자 enter ->")
                self.go_home()
            else:
                self.go_lotto()
        else:
            if self.min_money(MinMoneys.bowling_min.value):
                input("돈 없어. 집에 가자 enter ->")
                self.go_home()
            else:
                self.go_bowling()

        self.go()

    def min_money(self, min_money):
        return self.money < min_money

    def go(self):
        self.place.sub_menu()

    def go_home(self):
        self.place = home.Home(self.money)

    def go_lotto(self):
        self.place = lotto.Lotto(self.money)

    def go_bowling(self):
        self.place = bowling.Bowling(self.money)

    def values_chk(self, str):
        while True:
            try:
                num = int(str)
                return num
            except:
                str = input("숫자만 입력해주세요: ")
                return self.values_chk(str)


user_m = input("지금 돈 얼마 있어?\n입력: ")
a = Person(user_m)
a.sub_menu()