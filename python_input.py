# Date : 2023-09-06
# Author : J.H.Hwang
# Purpose :  입력을 연습하는 프로그램입니다.
# ------------------------------------------------
# 파이썬 입력
# 사용자의 입력을 받아 그 값을 프로그램에서 사용하고자 할 때 input() 함수를 사용 합니다.
# print("이름을 입력 하세요 : ", end=" ")

# name = input("이름을 입력 하세요 : ")
# # print(f"당신의 이름은 {name} 입니다.")
#
# # input 함수를 통해서 입력 받은 데이터는 문자열로 반환, 원하는 데이터 형으로 변환이 필요
# age = int(input("나이를 입력 하세요 : "))
# # print(f"당신의 나이는 {age}살 입니다.")
# # print(type(age))
#
# addr = input("주소를 입력 하세요 : ")
# jobs = input("직업을 입력 하세요 : ")
# score = float(input("성적을 입력 하세요 : "))
#
# print(f"안녕하세요? '{name}' 님 ")
# print(f"""당신의 주소는 {addr}이고,
# 직업은 {jobs}이며,
# 나이는 {age}살 이며,
# 성적은 {score}점 입니다.""")

#   split 함수는 기본은 공백 기준
# str1, str2 = input("이름과 주소 입력 : ").split()
# print(str1, str2)

# kor, eng, mat = map(int, input("국어 영어 수학 입력 : ").split())
# print(kor, eng, mat)

# val = list(map(int, input("성적 입력 : ").split()))
# print(type(val))

# ss = "a s d f"
# print(ss.split())

# hour, min, sec = input("시:분:초 : ").split(':')
# print(f"{hour}시 {min}분 {sec}초 입니다.")

# 시간을 24시간제이며 : 기준으로 입력 받은 후 오전과 오후로 출력 하도록 변경
hour, min, sec = map(int, input("시간 입력 : ").split(":"))
if(hour > 12):
    hour -= 12
    print(f"오후 {hour:02}시 {min:02}분 {sec:02}초")
else:
    print(f"오전 {hour:02}시 {min:02}분 {sec:02}초")