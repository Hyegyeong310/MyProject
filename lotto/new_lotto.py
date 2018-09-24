# new_lotto.py

import random, string


class Lotto:

    def __init__(self, money):
        self.money = money
        self.menu = ['로또구매', '당첨확인', '회차넘기기', '종료']

    def main_menu(self):

        print("="*25)
        print("로또 프로그램")
        print("="*25)

        count = 1
        for i in self.menu:
            print("{}. {}".format(count, i))
            count += 1

        choice = input("메뉴 입력: ")
        i = self.values_input(choice)

        if 0 < i < 5:
            if i == 1:
                self.buy_lotto()
            elif i == 2:
                self.chk_lotto()
            elif i == 3:
                self.next_lotto()
            elif i == 4:
                print("잘가요~")
        else:
            input("1~4 사이의 숫자만 입력해주세요\n다시 시작:")
            self.main_menu()

    def buy_lotto(self):
        print("게임 수를 입력하세요. 최대 20번까지 가능")

        num = input("게임 수: ")
        i = self.values_input(num)
        if 0 < i < 21:
            print("종류를 선택하세요.")
            choice = input("1. 자동\t2. 수동\t3. 뒤로가기: ")
            j = self.values_input(choice)
            if j == 1:
                self.buy_auto(j)
                self.left_money(j*5000)
            elif j == 2:
                self.buy_manual(j)
                self.left_money(j*5000)
            else:
                return self.main_menu()
        else:
            input("최대 20번까지 가능합니다\n다시 시작:")
            self.buy_lotto()

    def buy_auto(self, num):

        for i in range(0, num):
            lotto = random.sample(range(1, 46), 6)
            lotto.sort()
            print(lotto)

    def buy_manual(self, num):

        for i in range(0, num):
            manual_lotto = []
            for j in range(6):
                user_num = int(input("1~45 사이의 숫자를 입력하세요: "))
                if (user_num > 0) and (user_num < 46):
                    manual_lotto.append(user_num)
                else:
                    print("1~45 사이의 숫자만 입력해주세요.")
                    continue

    def chk_lotto(self):
        pass

    def next_lotto(self):
        pass

    def left_money(self, newMoney):
        self.money = self.money-newMoney
        print("남은 돈: {}".format(self.money))

    def values_input(self, str):
        while True:
            try:
                return int(str)
            except:
                str = input("숫자만 입력하세요: ")
                continue

user_money = 1000000
a = Lotto(user_money)
a.main_menu()
