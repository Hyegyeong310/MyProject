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


        while True:
            choice = input("메뉴 입력: ")
            choice = self.is_int(choice)

            if choice == 1:
                self.buy_lotto()
            elif choice == 2:
                self.chk_lotto()
            elif choice == 3:
                self.next_lotto()
            elif choice == 4:
                print("잘가요~")
                break
            else:
                pass

    def buy_lotto(self):
        print("게임 수를 입력하세요. 최대 20번까지 가능")

        num = input("게임 수: ")
        while self.is_int(num):
            num = int(num)
            if (num > 0) and (num < 21):
                print("종류를 선택하세요.")
                choice = input("1. 자동\t2. 수동\t3. 뒤로가기: ")

                if choice == "1":
                    self.buy_auto(num)
                    self.left_money(num*5000)
                elif choice == "2":
                    self.buy_manual(num)
                    self.left_money(num*5000)
                else:
                    self.main_menu()
                    break
            else:
                print("최대 20번까지 가능합니다.")

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

    def is_int(self, num):
        try:
            num = int(num)
            return num
        except:
            print("숫자만 입력하세요.")

user_money = 1000000
a = Lotto(user_money)
a.main_menu()
