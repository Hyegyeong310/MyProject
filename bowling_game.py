# bowling_game.py

import random

class BowlingGame:
    def __init__(self):
        self.rolls = {}  # 각 프레임별 점수
        self.resultList = []  # 프레임별 합 리스트
        self.players = 0  # 플레이어 수

    # player 수 입력
    def player(self):
        print("참가인원은 몇 명입니까? 최대 4명까지 가능")
        try:
            self.players = int(input("인원: "))
            while self.players < 0 or self.players > 4:
                self.players = int(input("최소 1명, 최대 4명까지 가능합니다. 다시 입력해주세요.\n인원: "))

            # for i in range(self.players):
            #     print("\n%d Player" % (i + 1))
            self.score()
        except:
            print("잘못 입력하셨습니다.")
            self.player()

    # 각 프레임별 핀수 랜덤 생성
    def roll(self):

        for i in range(10):
            framePin = []
            for j in range(2):
                pins = random.randint(10)
                if j > 0:
                    pins = random.randint(0, (10 - framePin[j - 1]))
                framePin.append(pins)
            self.rolls[i] = framePin
        # print(self.rolls)

    # 점수 계산
    def score(self):

        self.roll()

        result = 0
        rollIndex = 0
        self.resultList = []
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1

            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 1

            else:
                result += self.frameScore(rollIndex)
                rollIndex += 1
            self.resultList.append(result)

        self.showScore(self.rolls, self.resultList)
        # print(self.resultList)
        # return result

    # Strike 검사
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex][0] == 10

    # Spare 검사
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex][0] + self.rolls[rollIndex][1] == 10

    # Strike일 때 점수 계산
    def strikeScore(self, rollIndex):
        if rollIndex + 1 == 10:
            return 10
        else:
            return 10 + self.rolls[rollIndex + 1][0] + self.rolls[rollIndex + 1][1]

    # Spare일 때 점수 계산
    def spareScore(self, rollIndex):
        if rollIndex + 1 == 10:
            return 10
        else:
            return 10 + self.rolls[rollIndex + 1][0]

    # 프레임별 점수 계산
    def frameScore(self, rollIndex):
        return self.rolls[rollIndex][0] + self.rolls[rollIndex][1]

    # 점수 보이기
    def showScore(self, rolls, resultList):

        for i, val in rolls.items():
            if val[0] == 10:
                val[0] = "X"
            elif val[1] == (10 - val[0]):
                val[1] = "/"
            else:
                pass

        for a in range(10):
            print("*" * 10, end='\t')
        print(" ")

        for b in range(10):
            print("   %d회차   " % (b + 1), end='\t')
        print(" ")

        for c in range(10):
            print("*" * 10, end='\t')
        print(" ")

        for i in range(self.players):
            print("Player %d" % (i + 1))

            for d in range(10):
                print("  {} | {}  ".format(rolls[d][0], rolls[d][1]), end='\t')
            print(" ")

            for e in range(10):
                print("-" * 10, end='\t')
            print(" ")

            for f in range(10):
                print("    %d   " % resultList[f], end='\t')
            print(" ")


huns = BowlingGame()
huns.player()
