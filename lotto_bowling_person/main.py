"""person.py main 파일"""
from common_func import CommonFunc
from person import Person

if __name__ == "__main__":
    USER_MONEY = input("지금 돈 얼마 있어?\n입력: ")
    USER_MONEY = CommonFunc.values_chk(USER_MONEY)

    PERSON = Person(USER_MONEY)
    PERSON.sub_menu()
