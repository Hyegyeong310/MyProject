# new_lotto.py

import random


class Lotto:

    # 초기화
    def __init__(self, money):
        self.money = money
        self.menu = ['로또구매', '당첨확인', '회차넘기기', '종료']
        self.user_lottos = {}
        self.l_index = 1
        self.win_nums = []

    # 메인 메뉴
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
            input("1~4 사이의 숫자만 입력해주세요\n다시 시작 enter:")
            self.main_menu()

    # 로또 게임수
    def buy_lotto(self):
        print("게임 수를 입력하세요. 최대 20번까지 가능")

        times = input("게임 수: ")
        i = self.values_input(times)
        if 0 < i < 21:
            self.lotto_kinds(i)

        else:
            input("최대 20번까지 가능합니다\n다시 시작 enter:")
            self.buy_lotto()

    # 로또 종류 선택(자동, 수동)
    def lotto_kinds(self, times):

        print("종류를 선택하세요.")
        choice = input("1. 자동\t2. 수동\t3. 뒤로가기: ")
        j = self.values_input(choice)
        if 0 < j < 4:
            if j == 1:
                self.buy_auto(times)
                self.left_money(times * 5000)
            elif j == 2:
                self.buy_manual(times)
                self.left_money(times * 5000)
            else:
                return self.main_menu()

            a = input("다시 하시겠습니까?\n1. 네     2. 아니오")
            self.re_buy(a)
        else:
            input("1~3사이의 숫자만 입력하세요\n다시 시작 enter:")
            return self.lotto_kinds(times)

    # 로또 다시 구매
    def re_buy(self, ans):

        a2 = self.values_input(ans)
        if 0 < a2 < 3:
            if a2 == 1:
                self.buy_lotto()
            else:
                self.main_menu()
        else:
            print('1또는 2만 입력해주세요.')
            return self.re_buy()

    # 자동 구매
    def buy_auto(self, num):

        for i in range(0, num):
            lotto = random.sample(range(1, 46), 6)
            lotto.sort()
            print("{}번째 {}".format(i+1, lotto))
            self.user_lottos[self.l_index] = lotto
            self.l_index += 1

    # 수동 구매
    def buy_manual(self, num):

        for i in range(0, num):
            manual_lotto = []
            for j in range(1, 7):
                while True:
                    print('{}번째 숫자를 입력: '.format(j), end='')
                    num = input()
                    num = self.values_input(num)
                    if num not in range(1, 46):
                        print('1~45 사이 숫자만 입력하세요.')
                        continue
                    if num in manual_lotto:
                        x = manual_lotto.index(num) + 1
                        print("{}번째 숫자랑 중복입니다.".format(x))
                        continue
                    manual_lotto.append(num)
                    manual_lotto.sort()
                    break

            print("{}번째 {}".format(i + 1, manual_lotto))
            self.user_lottos[self.l_index] = manual_lotto
            self.l_index += 1

    # 당첨 확인
    def chk_lotto(self):
        if len(self.win_nums) == 0:
            self.win_lotto()

        # 구매한 로또
        if len(self.user_lottos) == 0:
            input("현재 구매한 로또가 없습니다 enter ->")
            return self.main_menu()
        else:
            print("현재 구매한 로또는 {}장 있습니다.".format(len(self.user_lottos)))
            print("이번 주 로또 번호: {}, 보너스: {}".format(self.win_nums[0], self.win_nums[-1]))
            for i, val in self.user_lottos.items():
                self.count_win(val)

            print("모두 확인했습니다.\n1. 다시확인   2. 메인으로")
            a = input()
            a2 = self.values_input(a)
            while True:
                if 0 < a2 < 3:
                    if a2 == 1:
                        return self.chk_lotto()
                    else:
                        return self.main_menu()
                else:
                    print("1 또는 2만 입력")
                    continue

    # 당첨번호 추출
    def win_lotto(self):
        win_num = random.sample(range(1, 46), 6)
        win_num.sort()
        self.win_nums.append(win_num)
        while True:
            b_num = random.randint(1, 46)
            if b_num not in self.win_nums:
                self.win_nums.append(b_num)
                break
            else:
                b_num = random.randint(1, 46)

    # 일치숫자 확인
    def count_win(self, lst):
        match_num = []
        for x in self.win_nums[0]:
            if x in lst:
                match_num.append(x)

        print("내 로또: {}".format(lst))
        print("{}개 일치\n일치한 번호: {}".format(len(match_num), match_num))
        input("다음 로또 확인 enter ->")

    # 회차 넘기기
    def next_lotto(self):
        print("다음 회차로 넘기겠습니까?\n1. 네  2. 아니오")
        a = input()
        a2 = self.values_input(a)
        if 0 < a2 < 3:
            if a2 == 1:
                self.win_nums = []
                self.user_lottos = {}
        else:
            print("1 또는 2로 답해주세요.")
            return self.next_lotto()

    # 남은 자금
    def left_money(self, newMoney):
        self.money = self.money-newMoney
        print("남은 돈: {}".format(self.money))

    # input 값 숫자 체크
    def values_input(self, str):
        while True:
            try:
                num = int(str)
                return num
            except:
                str = input("숫자만 입력하세요: ")
                continue

# 초기 자본금
user_money = 1000000

a = Lotto(user_money)
a.main_menu()
