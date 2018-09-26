# person.py

import random


class Lotto(object):
    def __init__(self, money):
        self.money = money
        self.menu = ["로또구매", "당첨확인", "회차넘김", "집으로"]
        self.place = None
        self.user_lottos = {}
        self.l_index = 1
        self.win_nums = []
        self.receipt_m = []

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
                print("="*25)
                print("당첨확인")
                print("="*25)
                if len(self.user_lottos) == 0:
                    input("구매한 로또가 없습니다.\n사러가기 enter ->")
                    return self.buy_lotto()
                else:
                    print("현재 {}장 있습니다.".format(len(self.user_lottos)))
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
        if len(self.user_lottos) >= 60:
            input("최대 30만원까지 구매 가능합니다 enter ->")
            self.sub_menu()
        else:
            print("몇 장 구매하시겠습니까? (최대 20장 가능)")
            count = input("개수: ")
            c2 = self.values_chk(count)
            if len(self.user_lottos) + c2 > 60:
                print("최대 30만원까지 구매 가능합니다.")
                print("현재 구매 가능한 개수는 {}입니다.".format(60-len(self.user_lottos)))
                return self.buy_lotto()
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
                self.left_money(num * 5000, False)
                self.again()
            elif c2 == 2:
                for i in range(num):
                    self.buy_manual()
                    print("{}번째 {}".format(i+1, self.user_lottos[self.l_index-1]))
                self.left_money(num * 5000, False)
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
        num.sort()
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
        if len(self.win_nums) == 0:
            self.make_win()
        print("{}, bonus: {}".format(self.win_nums[0], self.win_nums[1]))
        count = 1
        is_b = False
        for i, val in self.user_lottos.items():
            match_num = []
            input("로또 확인 enter ->")
            print("{}번째: {}".format(count, val))
            count += 1
            for x in self.win_nums[0]:
                if x in val:
                    match_num.append(x)
                    match_num.sort()
            if len(match_num) == 5 and self.win_nums[1] in val:
                is_b = True

            if is_b:
                print("{}개 일치: {} + Bonus [{}]".format(len(match_num), match_num, self.win_nums[1]))
            else:
                if len(match_num) == 0:
                    print("0개 일치")
                else:
                    print("{}개 일치: {}".format(len(match_num), match_num))

            self.chk_rank(i, match_num, is_b)
            if 3 <= len(match_num) <= 6:
                self.receipt_m.append(i)
        self.win_chk_again()

    def chk_rank(self, l_index, lst, is_b):
        ranks = [1658710563, 62592852, 1475065, 50000, 5000, 0]
        i = 0

        if len(lst) == 6:
            print("축하합니다. 1등 당첨!!")
            print("당첨금: {}".format(ranks[i]))
        elif len(lst) == 5:
            if is_b:
                i += 1
                print("축하합니다. 2등 당첨!!")
                print("당첨금: {}".format(ranks[i]))
            else:
                i += 2
                print("축하합니다. 3등 당첨!!")
                print("당첨금: {}".format(ranks[i]))
        elif len(lst) == 4:
            i += 3
            print("축하합니다. 4등 당첨!!")
            print("당첨금: {}".format(ranks[i]))
        elif len(lst) == 3:
            i += 4
            print("축하합니다. 5등 당첨!!")
            print("당첨금: {}".format(ranks[i]))
        else:
            i += 5

        if l_index in self.receipt_m:
            print("이미 수령한 로또입니다.")
            print("남은 돈: {}".format(self.money))
        else:
            self.left_money(ranks[i], True)

    def make_win(self):
        num = random.sample(range(1, 46), 6)
        num.sort()
        self.win_nums.append(num)
        while True:
            b_num = random.randint(1, 46)
            if b_num in num:
                b_num = random.randint(1, 46)
            else:
                self.win_nums.append(b_num)
                break

    def win_chk_again(self):
        print("다시 확인하시겠습니까? 1. 네    2. 아니오")
        choice = input("입력: ")
        c2 = self.values_chk(choice)
        if c2 == 1:
            return self.chk_win()
        elif c2 == 2:
            return self.sub_menu()
        else:
            print("1 또는 2만 입력하세요.")
            return self.win_chk_again()

    def next_lotto(self):
        print("다음 회차로 넘기시겠습니까? 1. 네    2. 아니오")
        choice = input("입력: ")
        c2 = self.values_chk(choice)
        if c2 == 1:
            self.win_nums = []
            self.user_lottos = {}
            return self.sub_menu()
        elif c2 == 2:
            return self.sub_menu()
        else:
            print("1 또는 2만 입력하세요.")
            return self.next_lotto()

    def left_money(self, newMoney, is_win):
        if is_win:
            self.money = self.money + newMoney
        else:
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


class Bowling(object):
    def __init__(self):
        pass

    def sub_menu(self):
        pass


class Home(object):
    def __init__(self):
        pass

    def sub_menu(self):
        print("집 도착!")

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