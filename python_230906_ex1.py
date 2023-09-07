# Date : 2023-09-06
# Author : J.H.Hwang
# Purpose :  오늘 배운것을 연습하는 예제 프로그램입니다.
# ------------------------------------------------
# 1. 정해진 형식으로 시간을 입력 받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분 05초
# while True:
#     time = input("시간을 입력해주세요 : ")
#     if time == "exit":
#         print("시간 입력을 종료합니다.")
#         break
#     else:
#         hour, mint, sec = map(int, time.split(":"))
#
#         if hour >= 12:
#             hour =  str((hour) - 12)
#             print(f"오후 {hour:02}시 {mint:02}분 {sec:02}초")
#         else:
#             print(f"오전 {hour:02}시 {mint:02}분 {sec:02}초")

# 2. 3개의 정수를 입력 받아 최대값과 최소값 구하기
# while True:
#     nums = input("정수을 입력해주세요 : ")
#     if nums == "exit":
#         print("정수 입력을 종료합니다.")
#         break
#     else:
#         nums_list = list(map(int, nums.split(" ")))
#         print(f"최소 : {min(nums_list)} 최대 : {max(nums_list)}")

# 3. 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
from datetime import datetime

while True:
    curr_year = datetime.today().year
    regi_num = input("주민등록번호를 입력해주세요 : ")
    if regi_num == "exit":
        print("주민등록번호 입력을 종료합니다.")
        break
    else:
        year = regi_num[:6][:2]
        mon = regi_num[:6][2:4]
        day = regi_num[:6][4:6]
        gender_num = regi_num[7]
        print(gender_num)
        print(f"curr_year = {curr_year}")
        print(f"jumin = {(1900 + int(regi_num[:2]))}")
        print(f"age = {curr_year - (1900 + int(regi_num[:2]))}")
        print(f"age = {str(curr_year - (1900 + int(regi_num[:2])))}")
        jumin_num = regi_num[:2]

        if int(gender_num) in [1, 2, 5, 6]:
            age = str(curr_year - (1900 + int(jumin_num)))
        else:
            age = str(curr_year - (2000 - int(jumin_num)))
        # 940312 - 1265466
        if gender_num == 1 or gender_num == 3:
            gender = "M"
        else:
            gender = "W"

        print(f"생년월일 : {year}년 {mon}월 {day}일 \n성별 : {gender} \n나이 : {age}")



# 4. 갯수가 정해지지 않은 여러 개의 정수를 입력 받아 합계와 평균 구하기
# while True:
#     nums = input("정수을 입력해주세요 : ")
#     if nums == "exit":
#         print("정수 입력을 종료합니다.")
#         break
#     else:
#         nums_list = list(map(int, nums.split(" ")))
#         print(f"합계 : {sum(nums_list)} 평균 : {sum(nums_list)/len(nums_list)}")