import random
from enum import Enum
from common_func import CommonFunc


ONE_PRICE = 3000

class BaseMenu(Enum):
    Play_Game = 1
    Home = 2

class Baseball:
    def __init__(self, person):
        self.person = person
        self.money = person.money

        self.num = [] # 기계 번호
        self.user_num = [] # 유저 번호
        self.b_count = 0 # ball 횟수
        self.s_count = 0 # Strike 횟수
        self.t_count = 0 # 시도 횟수

    def sub_menu(self):
        print("숫자 야구 시작~")
        for i in BaseMenu:
            print("{}. {}".format(i.value, i.name))
        print("")
        choice = input("입력: ")
        c2 = CommonFunc.values_chk(choice)
        if c2 == BaseMenu.Play_Game.value:
            self.start_game()
        elif c2 == BaseMenu.Home.value:
            self.person.go_home()
            self.person.go()
        else:
            input("1~2 중 선택하세요 enter ->")
            self.sub_menu()

    def user_answer(self):
        self.user_num = []
        for i in range(3):
            answer = input("{}번째 숫자를 입력해주세요: ".format(i+1))
            answer = CommonFunc.values_chk(answer)
            while answer in self.user_num:
                print("중복되는 숫자가 있습니다.")
                answer = input("{}번째 숫자를 입력해주세요: ".format(i + 1))
                answer = CommonFunc.values_chk(answer)
            self.user_num.append(answer)
        print("입력한 수: {}".format(self.user_num))
        self.is_strike_ball()

    def make_num(self):
        self.num = random.sample(range(1,10),3)

    def start_game(self):
        if not self.num:
            self.make_num()
        while self.t_count < 11:
            if self.s_count == 3:
                print("{}번만에 성공!".format(self.t_count))
                self.money = CommonFunc.left_money(self.money, ONE_PRICE, False)
                print("남은 돈: {}".format(self.money))
                input("메인으로 -> enter")
                self.sub_menu()

            else:
                self.t_count += 1
                print()
                print("{}번째 시도".format(self.t_count))
                self.user_answer()
                print("{} ball, {} strike!".format(self.b_count, self.s_count))
        else:
            print("실패...ㅜㅜ")
            self.money = CommonFunc.left_money(self.money, ONE_PRICE, False)
            print("남은 돈: {}".format(self.money))
            input("메인으로 -> enter")
            self.sub_menu()

    def is_strike_ball(self):
        self.s_count = 0
        self.b_count = 0
        for i in range(0,3):
            for j in range(0,3):
                if self.num[i] == self.user_num[j]:
                    if i == j:
                        self.s_count += 1
                    else:
                        self.b_count += 1
