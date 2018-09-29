from enum import Enum
import lotto
import bowling
import person


class HomeMenu(Enum):
    로또사러 = 1
    볼링치러 = 2
    밖으로 = 3
    종료 = 4


class Home(object):
    def __init__(self, money):
        self.money = money
        self.place = None

    def sub_menu(self):
        print("집 도착!")
        for i in HomeMenu:
            print("{}. {}".format(i.value, i.name))
        choice = input("입력: ")
        c2 = self.values_chk(choice)
        if c2 == HomeMenu.로또사러.value:
            self.place = lotto.Lotto(self.money)
        elif c2 == HomeMenu.볼링치러.value:
            self.place = bowling.Bowling(self.money)
        elif c2 == HomeMenu.밖으로.value:
            self.place = person.Person(self.money)
            self.place.sub_menu()
        elif c2 == HomeMenu.종료.value:
            print("빠잉~!")
            pass
        else:
            print("1~4 사이의 수만 입력하세요.")
            return self.sub_menu()

    def values_chk(self, str):
        while True:
            try:
                num = int(str)
                return num
            except:
                str = input("숫자만 입력해주세요: ")
                return self.values_chk(str)