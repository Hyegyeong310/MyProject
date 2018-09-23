# lotto_program_ver1.py

import random, string

cn = "y"

print("-"*25)
print("로또 번호 자동 생성기")
print("-"*25)
print("게임 수를 입력하세요(숫자만 입력)")

while(cn == "y" or cn == "Y"):

    num = input("게임 수: ")

    if(num.isdigit() == True):
        print("-"*25)

        for i in range(0,int(num)):
            lotto = random.sample(range(1,46),6)
            lotto.sort()
            print(lotto)
            cn = "n"
    else:
        print("-"*25)
        print("숫자를 입력하세요.")
        continue

    print("-"*25)
    print("로또 번호 생성 완료")
    print("-"*25)
    cn = input("다시 하시겠습니까(Y/N)? : ")

    while(cn != "y" and cn != "n" and cn != "Y" and cn != "N"):
        print("y나 n만 입력하세요.")
        print("-"*25)
        cn = input("다시 하시겠습니까(Y/N)? : ")

print("-"*25)
print("로또 번호 자동 생성 종료")