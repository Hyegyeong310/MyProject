

class CommonFunc:

    def values_chk(self, text):
        while True:
            try:
                num = int(text)
                return num
            except:
                text = input("숫자만 입력해주세요: ")
                return self.values_chk(text)