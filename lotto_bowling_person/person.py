# person.py

import random


class Lotto(object):
    def __init__(self, money):
        self.money = money

    def menu(self):
        pass


class Bowling(object):
    def __init__(self):
        pass

    def menu(self):
        pass


class Home(object):
    def __init__(self):
        pass

    def menu(self):
        pass

class Person(object):

    def __init__(self):
        self.money = 1000000
        self.menu = ["집으로 간다.", "로또사러 간다.", "볼링치러 간다."]
        self.place = None

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
                self.go_home()
            elif choice == 2:
                print("로또사러 왔다.")
                self.go_lotto()
            else:
                print("볼링치러 왔다.")
                self.go_bowling()

            self.go()
        else:
            input("1~3 사이의 번호를 입력해주세요 enter->")
            return self.main_menu()

    def go(self):
        self.place.menu()

    def go_home(self):
        self.place = Home()

    def go_lotto(self):
        self.place = Lotto(self.money)

    def go_bowling(self):
        self.place = Bowling()

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