# # ======================== 완성 ==========================
def scores_and_count():
    while True:
        input_str_list = list(map(int, input().split(" ")))
        if input_str_list[0] != len(input_str_list[1:]):
            print("점수의 수가 다릅니다. 다시 입력하세요.")
        elif [i for i in input_str_list[1:] if not 0 < i <= 100]:
            print("100점을 초과한 값이 있습니다. 다시 입력하세요.")
        else:
            return input_str_list[0], input_str_list[1:]

def student_filter(student_count, student_scores):
    cnt = 0
    for e in student_scores:
        if e > sum(student_scores)/student_count:
            cnt += 1
    return round((cnt/len(student_scores) * 100), 3)

def print_scores(result_list):
    for i in result_list:
        print(f"{i}%")

result_list = []
test_count = int(input())
for _ in range(test_count):
    student_count, student_scores = scores_and_count()
    result = student_filter(student_count, student_scores)
    result_list.append(result)
print_scores(result_list)

# ======================= 강사님이 푼 것 ============================
# def over_rate():    # 각 케이스에서 평균이 넘는 비율 구하기
#     ls = list(map(int, input().split()))    # 입력을 받아 공백 기준으로 입력 받아서 정수형 리스트로 담음
#     average = sum(ls[1:]) / len(ls[1:])     # 리스트에서 맨 앞의 요소는 인원수이므로 제외, 총합 / 인원 수 = 평균
#     cnt = 0     # 평균이 넘는 % 를 구하기 위해서는 인원에 카운트가 필요
#     for i in range(1, len(ls)):     # 맨 앞은 빼야 하므로 1부터 돌린다
#         if ls[i] > average: cnt += 1
#     return cnt / (len(ls) - 1) * 100    # 백분율 표기로 변경
#
# n = int(input())    # 총 테스트 횟수
# rst = [] # 각 케이스에 대한 결과값을 받기 위한 리스트
# for i in range(n):  # 총 테스트 횟수 만큼 반복 수행
#     rst.append(over_rate())
#
# for e in rst:
#     print(f"{e:.3f}%")      # 소수점 3번째 자리에서 반올림


# ================ 맨 처음 코드 ==================

# test_count = int(input())
# result_ls = []
# for _ in range(test_count):
#     in_str_ls = input().split(" ")
#     int_ls = list(map(int, in_str_ls))
#     int_ls_score = int_ls[1:]
#     if int_ls[0] == len(int_ls_score):
#         cnt = 0
#         for e in int_ls_score:
#             if e > sum(int_ls_score)/len(int_ls_score):
#                 cnt += 1
#         result_ls.append(round((cnt/len(int_ls_score) * 100), 3))
#     else:
#         print("잘못됐습니다")
#         break
# for i in result_ls:
#         print(f"{i}%")