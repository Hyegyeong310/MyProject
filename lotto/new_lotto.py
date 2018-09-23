# new_lotto.py

import random, string

class Lotto(object):
    def __init__(self, money):
        self.money = money
        self.menu = ['로또구매', '당첨확인', '회차넘기기', '종료']

    def main_menu(self):
        check = "y"
        count = 1

        while check == "y":

            print("="*25)
            print("로또 프로그램")
            print("="*25)

            for i in self.menu:
                print("%d. %s" % (count, i))
                count += 1

            choice = input("메뉴 입력: ")
            if(choice.isdigit() == True):
                if choice == "1":
                    self.buy_lotto()
                elif choice == "2":
                    self.chk_lotto()
                elif choice == "3":
                    self.next_lotto()
                elif choice == "4":
                    print("잘가요~")
                    check = "n"
                else:
                    pass
            else:
                print("1에서 4까지의 숫자를 입력하세요.")
                continue

    def buy_lotto(self):
        check = "y"

        print("게임 수를 입력하세요.")
        while check == "y":
            num = input("게임 수: ")
            if(num.isdigit() == True):

                print("종류를 선택하세요.")
                choice = input("1. 자동\t2. 수동\t3. 뒤로가기: ")
                if(choice.isdigit() == True):

                    if choice == "1":
                        self.buy_auto(int(num))
                        check = "n"
                    elif choice == "2":
                        self.buy_manual(int(num))
                        check = "n"
                    else:
                        self.main_menu()
                else:
                    print("숫자를 입력하세요.")
                    continue
            else:
                print("숫자를 입력하세요.")
                continue

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
                if (user_num > 0 and user_num < 46):
                    manual_lotto.append(user_num)
                else:
                    print("1~45 사이의 숫자만 입력해주세요.")
                    continue

    def chk_lotto(self):
        pass

    def next_lotto(self):
        pass


user_money = 1000000
a = Lotto(user_money)
a.main_menu()
