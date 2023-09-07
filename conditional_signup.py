# Date : 2023-09-07
# Author : J.H.Hwang
# Purpose :  제어문으로 회원가입을 만들어 보는 프로그램입니다.
# ------------------------------------------------
user = input("아이디 입력 : ")
if len(user) >= 8 :    # 입력 받은 아이디의 길이가 10과 같거나 커야 함
    pw = input("비밀번호 입력 : ")
    # if pw.__len__() < 8 or pw.__len__() > 16:
    if len(pw) < 8 or len(pw) > 16:
        print("비밀번호는 8자에서 16자 사이여야 합니다.")
    elif pw.find(user) >= 0:
        print("비밀번호에 아이디를 포함시킬 수 없습니다.")
    else:
        print(f"아이디 : {user}")
        print(f"패스워드 : {pw}")
else:
    print("아이디는 반드시 8자리 이상이어야 합니다.")