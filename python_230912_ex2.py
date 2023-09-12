# A = 2100000000
# B = 9
# C = 10
# n = 1
#
# print(round(A * (1-(B/C))) + 1)
#
# while True:
#     if A + (B * n) - (C * n):
#         n += 1
#     else:
#         break
# print((n) + 1)

# ================== 강사님이 푼 것 ===================
# 고정 비용 : 1000
# 가변 비용 : 70
# 판매 비용 : 170

fix, var, sell = map(int, input().split())
# cnt = 0
# while True:
#     # if fix + (var * cnt) < sell * cnt : break
#     if cnt > fix // (sell - var): break
#     cnt += 1
#
#
# print(cnt)
if sell <= var: print(-1)
else: print(fix // (sell - var) + 1)

