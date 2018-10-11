

class CommonFunc:

    @staticmethod
    def values_chk(text):
        while True:
            try:
                num = int(text)
                return num
            except:
                text = input("숫자만 입력해주세요: ")
                return CommonFunc.values_chk(text)

    @staticmethod
    def left_money(money, new_money, is_win):

        c_money = 0

        if is_win:
            c_money = money + new_money
        else:
            c_money = money - new_money

        return c_money
