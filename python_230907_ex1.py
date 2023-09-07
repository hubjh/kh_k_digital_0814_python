# Date : 2023-09-07
# Author : J.H.Hwang
# Purpose :  제어문 예제 프로그램입니다.
# ------------------------------------------------

# 1번 문제 : 세 자리 정수를 입력 받은 후 가장 큰 수 찾기 (123 => 3)
# while True:
#     in_num = input("세자리 정수를 입력해주세요 : ")
#     if len(in_num) == 3:
#         num_list = list(map(int, in_num))
#         print(max(num_list))
#     elif in_num == "exit":
#         print("반복 종료")
#         break
#     else:
#         print("세자리 정수가 아닙니다. 다시 입력 해주세요.")
# 2번 문제 : 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 근무 : 9620원


# JUGAN = 9620
# # 야간 근무 : 주간 시급 * 1.5
# YAGAN = JUGAN * 1.5
# # 주간 근무 [1], 야간근무[2]를 입력 하세요 :
# while True:
#     work_inp = input("주간 근무 [1], 야간근무[2]를 입력 하세요 :")
#     if work_inp == "1":
#         work_type = 1
#         break
#     elif work_inp == "2":
#         work_type = 2
#         break
#     else:
#         print("잘못 입력했습니다. [1] [2] 둘 중 하나만 입력해주세요.")
# # 근무 시간을 입력 해주세요 :
# while True:
#     work_time = int(input("근무 시간을 입력 해주세요 :"))
#     # 입력한 시간 동안 근무한 주간 또는 야간 급여는 ___원 입니다.
#     if work_time > 0 and work_time < 24:
#         if work_type == 1:
#             print(f"입력한 시간 동안 주간 급여는 {JUGAN * work_time}원 입니다.")
#             break
#         if work_type == 2:
#             print(f"입력한 시간 동안 주간 급여는 {YAGAN * work_time}원 입니다.")
#             break
#     else:
#         print("잘못 입력했습니다. 1 ~ 23시간 중에서 입력해주세요.")

# 3번 문제 : 문자열 추가하기
# 2개의 문자열을 포인터 변수 s와 k에,
# 양의 정수를 정수형 변수 n에 각각 전달 받아 s 문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성
# s : seoul
# k : korea
# n : 2
# 결과 : ulkorea

s = input("문자를 입력해주세요 : ")

k = input("문자를 입력해주세요 : ")

n = int(input("숫자를 입력해주세요 : "))

print(f"{s[-n:] + k}")



