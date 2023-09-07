# Date : 2023-09-06
# Author : J.H.Hwang
# Purpose :  출력 연습하는 프로그램입니다.
# ------------------------------------------------
# 파이썬의 다양한 출력 방법
name = "곰돌이사육사"
age = 20
gender = "남성"
jobs = "소프트웨어 개발자"
addr = "서울시 강남구 역삼동"

# C 언어 스타일 : 서식지정자를 사용하는 방식
print("=" * 5, "C 스타일", "=" * 5)
print("이름 : %s" % name)
print("나이 : %d" % age)
print("성별 : %s" % gender)
print("직업 : %s" % jobs)
print("주소 : %s\n" % addr)

# Python 스타일 : 3.6 이전 방법
print("=" * 5, "Python 스타일 1", "=" * 5)
print("이름과 주소 : {} {}".format(name, addr))
print("나이 : {}".format(age))
print("성별 : {}".format(gender))
print("직업 : {}\n".format(jobs))

# Python 스타일 : 3.6 이후 방법
print("=" * 5, "Python 스타일 2", "=" * 5)
print(f"이름 : {name} \n성별 : {gender} \n나이 : {age} \n직업 : {jobs} \n주소 : {addr}\n")

# Java 스타일 : 문자열 연결 방법 (+)
print("=" * 5, "Java 스타일", "=" * 5)
print("이름 : " + name)
print("나이 : " + str(age))
print("성별 : " + gender)
print("직업 : " + jobs)
print("주소 : " + addr)

# 출력 시 정렬
num = 10
# < 좌측 정렬
print("|{:<5}|".format(10))
print(f"|{num:<5}|")

# > 우측 정렬, 생략 가능
print("|{:5}|".format(10))
print("|{:>5}|".format(10))
print(f"|{num:5}|")
print(f"|{10:>5}|")

# ^ 중앙 정렬
print("|{:^6}|".format(10))
print(f"|{num:^6}|")

PI = 3.14159265
print(f"{PI:.2f}")
print(f"{PI:.4f}")


