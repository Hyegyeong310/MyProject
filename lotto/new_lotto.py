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
        self.receipt_lotto = []

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
            return self.main_menu()

    # 로또 게임수
    def buy_lotto(self):
        if len(self.user_lottos) >= 60:
            input("30만원 이상 구매하실 수 없습니다.")
            return self. main_menu()
        else:
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
                self.left_money(times * 5000, False)
            elif j == 2:
                self.buy_manual(times)
                self.left_money(times * 5000, False)
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
            ans = input('1또는 2만 입력해주세요: ')
            return self.re_buy(ans)

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
            print("이번 주 로또 번호: {}, 보너스: {}".format(self.win_nums[0], self.win_nums[1]))
            for i, val in self.user_lottos.items():
                self.count_win(i, val)
                self.receipt_lotto.append(i)

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
    def count_win(self, i_lst, lst):
        match_num = []
        i = False
        for x in self.win_nums[0]:
            if x in lst:
                match_num.append(x)
        if len(match_num) == 5 and self.win_nums[1] in lst:
            i = True

        print("내 로또: {}".format(lst))
        if i:
            print("{}개 일치: {} + Bonus [{}]".format(len(match_num), match_num, self.win_nums[1]))
        else:
            print("{}개 일치: {}".format(len(match_num), match_num))

        self.chk_rank(i_lst, match_num, i)
        input("다음 로또 확인 enter ->")

    # 등수 체크
    def chk_rank(self, i_lst, lst, is_b):
        len_lst = len(lst)
        ranks = [1658710563, 62592852, 1475065, 50000, 5000, 0]
        i = 0

        if len_lst == 6:
            print("축하합니다 1등 당첨!")
            print("당첨금: {}".format(ranks[0]))
        elif len_lst == 5:
            if is_b:
                print("축하합니다 2등 당첨!")
                print("당첨금: {}".format(ranks[1]))
                i += 1
            else:
                print("축하합니다 3등 당첨!")
                print("당첨금: {}".format(ranks[2]))
                i += 2
        elif len_lst == 4:
            print("축하합니다 4등 당첨!")
            print("당첨금: {}".format(ranks[3]))
            i += 3
        elif len_lst == 3:
            print("축하합니다 5등 당첨!")
            print("당첨금: {}".format(ranks[4]))
            i += 4
        else:
            print("아쉽네요~")
            print("당첨금: 0")
            i += 5

        if i_lst in self.receipt_lotto:
            print("확인한 로또입니다.")
            print(self.money)
        else:
            self.left_money(ranks[i], True)


    # 회차 넘기기
    def next_lotto(self):
        print("다음 회차로 넘기겠습니까?\n1. 네  2. 아니오")
        a = input()
        a2 = self.values_input(a)
        if 0 < a2 < 3:
            if a2 == 1:
                self.win_nums = []
                self.user_lottos = {}
                input("회차 넘김 완료")
            return self.main_menu()
        else:
            print("1 또는 2로 답해주세요.")
            return self.next_lotto()

    # 남은 자금
    def left_money(self, newMoney, is_win):
        if is_win:
            self.money = self.money+newMoney
        else:
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
                return self.values_input(str)

# 초기 자본금
user_money = 1000000

a = Lotto(user_money)
a.main_menu()
