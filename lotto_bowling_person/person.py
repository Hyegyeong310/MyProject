# person.py

import random


class Lotto(object):
    def __init__(self, money):
        self.money = money
        self.menu = ["로또구매", "당첨확인", "회차넘김", "집으로"]
        self.place = None
        self.user_lottos = {}
        self.l_index = 1

    def sub_menu(self):
        for i in self.menu:
            print("{}. {}".format(self.menu.index(i)+1, i), end="\t")
        print("")
        choice = input("입력: ")
        c2 = self.values_chk(choice)
        if 0 < c2 < 5:
            if c2 == 1:
                print("로또구매")
                self.buy_lotto()
            elif c2 == 2:
                print("당첨확인")
                self.chk_win()
            elif c2 == 3:
                print("회차넘김")
                self.next_lotto()
            else:
                self.place = Home()
                self.place.sub_menu()

        else:
            input("1~4 중 선택하세요 enter ->")
            return self.sub_menu()

    def buy_lotto(self):
        print("몇 장 구매하시겠습니까? (최대 20장 가능)")
        count = input("개수: ")
        c2 = self.values_chk(count)
        if 0 < c2 < 21:
            self.chk_kinds(c2)
        else:
            print("최소 1장, 최대 20장이어야 합니다.")
            return self.buy_lotto()

    def chk_kinds(self, num):
        print("1. 자동    2. 수동   3. 뒤로가기")
        choice = input("입력: ")
        c2 = self.values_chk(choice)
        if 0 < c2 < 4:
            if c2 == 1:
                for i in range(num):
                    self.buy_auto()
                    print("{}번째 {}".format(i+1, self.user_lottos[self.l_index-1]))
                self.again()
            elif c2 == 2:
                for i in range(num):
                    self.buy_manual()
                    print("{}번째 {}".format(i+1, self.user_lottos[self.l_index-1]))
                self.again()
            if c2 == 3:
                return self.sub_menu()
        else:
            print("1~3 사이의 번호를 입력하세요.")
            return self.chk_kinds(num)

    def again(self):
        print("계속 구매하시겠습니까? 1. 네    2. 메인으로")
        choice = input("입력: ")
        c2 = self.values_chk(choice)
        if 0 < c2 < 3:
            if c2 == 1:
                return self.buy_lotto()
            else:
                return self.sub_menu()
        else:
            input("1 또는 2만 입력하세요 enter ->")
            return self.again()

    def buy_auto(self):
        num = random.sample(range(1, 46), 6)
        self.user_lottos[self.l_index] = num
        self.l_index += 1

    def buy_manual(self):
        nums = []
        for i in range(1, 7):
            while True:
                print("{}번째 수 입력: ".format(i))
                num = input()
                n2 = self.values_chk(num)
                if n2 not in range(1, 46):
                    print("1~45 사이의 수만 입력하세요.")
                    continue
                if n2 in nums:
                    x = nums.index(n2) + 1
                    print("{}번째 수와 중복입니다.".format(x))
                    continue
                nums.append(n2)
                nums.sort()
                break
        self.user_lottos[self.l_index] = nums
        self.l_index += 1

    def chk_win(self):
        pass

    def next_lotto(self):
        pass

    def values_chk(self, str):
        while True:
            try:
                num = int(str)
                return num
            except:
                str = input("숫자만 입력해주세요: ")
                return self.values_chk(str)


class Bowling(object):
    def __init__(self):
        pass

    def sub_menu(self):
        pass


class Home(object):
    def __init__(self):
        pass

    def sub_menu(self):
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
        c2 = self.values_chk(choice)
        if 0 < c2 < 4:
            if c2 == 1:
                print("집 도착!")
                self.go_home()
            elif c2 == 2:
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
        self.place.sub_menu()

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