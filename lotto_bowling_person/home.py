from enum import Enum
from common_func import CommonFunc


class HomeMenu(Enum):
    Lotto = 1
    Bowling = 2
    Baseball = 3
    Go_Outside = 4
    Exit = 5


class Home:
    def __init__(self, person):
        self.person = person

    def sub_menu(self):
        print("집 도착!")
        for i in HomeMenu:
            print("{}. {}".format(i.value, i.name))
        choice = input("입력: ")
        c2 = CommonFunc.values_chk(choice)

        if c2 == HomeMenu.Lotto.value:
            self.person.go_lotto()
            self.person.go()
        elif c2 == HomeMenu.Bowling.value:
            self.person.go_bowling()
            self.person.go()
        elif c2 == HomeMenu.Baseball.value:
            self.person.go_baseball()
            self.person.go()
        elif c2 == HomeMenu.Go_Outside.value:
            self.person.sub_menu()
        elif c2 == HomeMenu.Exit.value:
            print("빠잉~!")
            pass
        else:
            print("{}~{} 사이의 수만 입력하세요.".format(1, len(HomeMenu)))
            self.sub_menu()
