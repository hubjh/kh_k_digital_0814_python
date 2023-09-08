import random
# randint(0, 4) : 0 ~ 4 까지의 임의의 정수값이 반환
# randrange(0, 4): 0 ~ 4 미만의 임의의 정수값이 반환

for i in range(100):
    # rand = random.randint(0, 4)
    rand = random.randrange(0, 4)
    print(rand)

# 현재 시간 가져 오기
from datetime import datetime   # datetime.py 라는 파일에서 datetime 이라는 함수(클래스)를 가져오겠다.
datetime.today()

# import datetime
# datetime.datetime.today()       # 파일을 알려주지 않았기때문에 datetime(파일).datetime(클래스).today(메서드)

print(datetime.today()) # 현재 날짜 가져오기
print(datetime.today().year)
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

# 수학 계산을 위한 math

import math

print(math.sin(100))    # sin
print(math.cos(100))    # cos
print(math.tan(100))    # tan
print(math.log(100))    # log
print(math.ceil(100.1)) # 무조건 올림
print(math.floor(100.9999)) # 무조건 내림

# 중복 값이 없는 로또 번호 생성하기
import random
print("로또 번호 자동 생성기")
ls = [] # 빈 리스트 만들기
while True:
    rand = random.randrange(1, 46)
    if rand not in ls:  # list에 생성된 rand값이 포함되어 있지 않으면
        ls.append(rand)
    if len(ls) == 6: break
print(ls)