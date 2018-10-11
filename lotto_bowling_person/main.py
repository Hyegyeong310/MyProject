from common_func import CommonFunc
from person import Person

if __name__ == "__main__":
    user_money = input("지금 돈 얼마 있어?\n입력: ")
    user_money = CommonFunc.values_chk(user_money)

    person = Person(user_money)
    person.sub_menu()