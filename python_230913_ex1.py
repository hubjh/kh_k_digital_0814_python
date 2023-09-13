# # 1. 배수 찾기 (초급에 있음)
# # 큐형식
# tmp_ls = []
# while True:
#     inp_int = int(input())
#     if inp_int == 0: break
#     tmp_ls.append(inp_int)
#
# for e in tmp_ls[1:]:
#     if e % tmp_ls[0] == 0: print(f"{e} is a multiple of {tmp_ls[0]}.")
#     else: print(f"{e} is NOT a multiple of {tmp_ls[0]}.")

tmp_ls2 = []
while True:
    inp_ls = list(map(int, input().split()))
    if not (inp_ls[0] and inp_ls[1] and inp_ls[2]):
        break
    max_num = max(inp_ls)
    low_nums = [x for x in inp_ls if x != max_num]

    if max_num**2 - (low_nums[0]**2 + low_nums[1]**2) == 0:
        tmp_ls2.append('right')
    else:
        tmp_ls2.append('wrong')

for e in tmp_ls2:
    print(e)

# tmp1, tmp2 = map(int, input().split())
# print(tmp1 + tmp2)