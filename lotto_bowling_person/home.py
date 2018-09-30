from enum import Enum
import common_func
import person


class HomeMenu(Enum):
    Lotto = 1
    Bowling = 2
    Go_Outside = 3
    Exit = 4


class Home:
    def __init__(self, money, lotto, bowling):
        self.money = money
        self.lotto = lotto
        self.bowling = bowling
        self.person = person.Person(self.money)
        self.common = common_func.CommonFunc()

    def sub_menu(self):
        print("집 도착!")
        for i in HomeMenu:
            print("{}. {}".format(i.value, i.name))
        choice = input("입력: ")
        c2 = self.common.values_chk(choice)
        if c2 == HomeMenu.Lotto.value:
            self.lotto.sub_menu()
        elif c2 == HomeMenu.Bowling.value:
            self.bowling.sub_menu()
        elif c2 == HomeMenu.Go_Outside.value:
            self.person.sub_menu()
        elif c2 == HomeMenu.Exit.value:
            print("빠잉~!")
            pass
        else:
            print("1~4 사이의 수만 입력하세요.")
            return self.sub_menu()
