def scores_and_count():
    while True:
        input_str_list = input().split(" ")
        input_str_list = list(map(int, input_str_list))
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


# =========== 완성 =============
result_list = []
test_count = int(input())
for _ in range(test_count):
    student_count, student_scores = scores_and_count()
    result = student_filter(student_count, student_scores)
    result_list.append(result)
print_scores(result_list)


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