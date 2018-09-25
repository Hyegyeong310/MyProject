# person.py

import random


class Lotto(object):
    def __init__(self, money):
        self.money = money

    def lotto_menu(self):
        pass


class Bowling(object):
    def __init__(self):
        pass

    def bowling_menu(self):
        pass


class Person(Lotto, Bowling):

    def __init__(self):
        self.money = 1000000
        self.menu = ["집으로 간다.", "로또사러 간다.", "볼링치러 간다."]

    def main_menu(self):
        print("무엇을 할까~~")
        for i in self.menu:
            print("{}. {}".format((self.menu.index(i)+1), i), end="\t")
        print("")
        choice = input("입력: ")
        choice = self.values_chk(choice)
        if 0 < choice < 4:
            if choice == 1:
                print("집 도착!")
            elif choice == 2:
                print("로또사러 왔다.")
                Lotto.lotto_menu(self)
            else:
                print("볼링치러 왔다.")
                Bowling.bowling_menu(self)

        else:
            input("1~3 사이의 번호를 입력해주세요 enter->")
            return self.main_menu()

    def values_chk(self, str):
        while True:
            try:
                num = int(str)
                return num
            except:
                str = input("숫자만 입력해주세요: ")
                return self.values_chk(str)


a = Person()
a.main_menu()