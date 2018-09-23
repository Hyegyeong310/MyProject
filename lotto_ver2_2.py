import random

class Lotto(object):
    def __init__(self, money):
        self.money = money # 초기자본금
        self.menu = ['로또사기', '당첨확인', '회차넘기기', '종료']
        self.userLotto = {} # 유저 로또 dict
        self.winLotto = [] # 당첨 번호
        self.winIndex = [] # 당첨된 로또 인덱스
        self.LottoIndex = 1
        self.buyCount = 0

    def MainMenu(self): # 메인메뉴

        if len(self.winLotto) == 0:
            self.WinLotto() # 당첨번호 생성

        choice = 0
        while choice != 4:
            print("메뉴를 선택하세요.")
            for i in range(len(self.menu)):
                print("%d. %s" % (i+1, self.menu[i]))
            try:
                choice = int(input("\n메뉴 선택: "))

                if choice == 1: # 로또 사기
                    self.BuyLotto()

                elif choice == 2: # 당첨 확인
                    self.WinCheck()

                elif choice == 3: # 회차넘김
                    self.NextWin()

                elif choice == 4: # 종료
                    print('잘가요~~')
                    break

            except:
                print('\n잘못 입력하셨습니다.\n')

    def BuyLotto(self): # 로또 구매

        if self.buyCount < 60:

            print("몇 장 사시겠습니까? 최대 20장까지 구매 가능")
            try:
                count = int(input("수량: "))

                if count < 1 or count > 20:
                    print("최소 1장부터 최대 20장까지 가능합니다. 다시 입력해주세요.")
                    self.BuyLotto()

                else:
                    print("1. 자동, 2. 수동 3. 뒤로가기")
                    try:
                        choice = int(input('입력: '))

                        if choice == 1: # 자동
                            for i in range(count):
                                self.AutoLotto()
                                self.IndexLotto()
                            print("구매한 로또 번호")
                            for idx, j in self.userLotto.items():
                                print("%d번. %s" % (idx, str(j)))

                            self.leftMoney(count*5000, False)
                            self.buyCount += count
                        elif choice == 2: # 수동
                            for i in range(count):
                                print("수동 %d번째"% (i+1))
                                self.ManualLotto()
                                self.IndexLotto()
                            for idx,j in self.userLotto.items():
                                print("%d번. %s" % (idx, str(j)))

                            self.leftMoney(count*5000, False)
                            self.buyCount += count

                        elif choice == 3: # 메인 메뉴로 돌아가기
                            self.MainMenu()
                    except:
                        print('\n잘못 입력하셨습니다.\n')
                        self.BuyLotto()
            except:
                print('\n잘못 입력하셨습니다.\n')
                self.BuyLotto()

        else:
            print("하루 30만원 이상 구매할 수 없습니다.")
            self.MainMenu()

    def AutoLotto(self): # 자동
        userNumbers = []

        for i in range(0,6):
            number = random.randint(1, 46)
            while number in userNumbers:
                number = random.randint(1, 46)
            userNumbers.append(number)
        userNumbers.sort()
        self.userLotto[self.LottoIndex] = userNumbers
        # self.userLotto.append(userNumbers)

    def ManualLotto(self): # 수동
        userNumbers = []

        for j in range(0, 6):
            number = int(input("1에서 45까지의 수를 입력하세요. "))
            while number < 1 or number > 45:
                number = int(input("1에서 45까지의 수만 가능합니다. 다시 입력해주세요. "))
            while number in userNumbers:
                number = int(input("중복되는 수가 있습니다. 다시 입력해주세요. "))
            userNumbers.append(number)
        userNumbers.sort()
        self.userLotto[self.LottoIndex] = userNumbers
        # self.userLotto.append(userNumbers)

    def WinCheck(self): # 당첨확인
        print("이번 주 당첨 번호: ")
        print(self.winLotto)

        print("당신의 로또는 %d개 있습니다." % len(self.userLotto))

        for idx, i in self.userLotto.items():

            counter = 0
            same_num = []

            for number in i:
                if number in self.winLotto:
                    counter += 1
                    same_num.append(number)
            print("\n%d번 번호: %s" % (idx, i))
            print("일치하는 번호가 %d개 있습니다." % counter)
            if counter != 0:
                print("일치하는 번호: %s" % same_num )

            if counter > 2 :
                if counter == 3:
                    winMoney = 5000
                elif counter == 4:
                    winMoney = counter * 5000
                elif counter == 5:
                    winMoney = counter * 10000
                elif counter == 6:
                    winMoney = counter * 100000

                print("당첨금: %d" % winMoney)
                self.leftMoney(winMoney, True, idx)

            input("다음 확인 enter")
        print("구매하신 로또를 모두 확인했습니다. 확인한 로또를 지우시겠습니까? Y/N")
        answer = input("입력: ")
        if answer.upper() == "Y":
            self.userLotto = {}

    def NextWin(self): # 회차 넘기기
        print("다음 회차로 넘기시겠습니까? \n1. 네, 2. 아니오 3. 뒤로가기")
        choice = int(input("입력: "))
        try:
            if choice == 1:
                self.winIndex = []
                self.winLotto = []
                self.WinLotto()
                self.userLotto = {}
                self.buyCount = 0
            elif choice == 2 or choice == 3:
                self.MainMenu()
        except:
            print('\n잘못 입력하셨습니다.\n')
            self.NextWin()


    def WinLotto(self): # 당첨번호 생성
        for i in range(0, 6):
            number = random.randint(1, 46)
            while number in self.winLotto:
                number = random.randint(1, 46)

            self.winLotto.append(number)
        self.winLotto.sort()

    def leftMoney(self, newMoney, isWin, LIndex = None): # 남은 돈 계산

        if isWin:

            if LIndex not in self.winIndex:
                self.winIndex.append(LIndex)
                self.money = self.money + newMoney
            else:
                print("이미 당첨금을 수령하였습니다.")

        else:
            self.money = self.money - newMoney

        print(self.money)


    def IndexLotto(self):
        self.LottoIndex += 1

start_money = 1000000
huns = Lotto(start_money)
huns.MainMenu()
