def test_start():
    test_count = int(input())
    for _ in range(test_count):

def scores_and_count():
    input_str_list = input().split(" ")
    input_str_list = list(map(int, input_str_list))
    return

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