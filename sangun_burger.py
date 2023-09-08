# ==================== 상근날드 ======================
# food_ls = []
# while True:
#     food = int(input("음식 가격을 입력하세요 :"))
#     if 100 <= food <= 2000:
#         food_ls.append(food)
#     else:
#         print("다시 입력하세요.")
#     if len(food_ls) == 5: break
# print(min(food_ls[:3]) + min(food_ls[-2:]) - 50)


# ===================== 저항 =======================
# register = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
# str_ls = []
# while True:
#     input_str = input("색깔을 입력하세요 : ")
#     if input_str in register:
#         str_ls.append(input_str)
#     else:
#         print("다시 입력하세요.")
#     if len(str_ls) == 3: break
#
# print_rst = ""
# for i, elc in enumerate(str_ls):
#     if i == 0 or i == 1:
#         print_rst += str(register.index(elc))
#     else:
#         print_rst = int(print_rst) * (10 ** register.index(elc))
# print(print_rst)


# =================== pc 알바 =========================
# while True:
#     customer = int(input("손님의 수 : "))
#     if 0 < customer <= 100: break
#     else:
#         print("다시 입력하세요.")
#
# while True:
#     seat_nums = list(map(int, input("들어오고 싶어하는 자리 번호 : ").split()))
#     if 0 < len(seat_nums) <= 100 and len(seat_nums) == customer: break
#     else:
#         print("다시 입력하세요.")
#
# reserved_seats = []
# refuse_cnt = 0
# for i in seat_nums:
#     if i not in reserved_seats:
#         reserved_seats.append(i)
#     else:
#         refuse_cnt += 1

# print(f"거절된 횟수 : {refuse_cnt}")


# ====================== KMP, MS ====================
# KMP = "Knuth-Morris-Pratt"
# MS = "Mirko-Slavko"

# while True:
#     rst_ls = []
#     inp_total_str = input("문자를 입력하세요 : ")
#     if inp_total_str == "exit":
#         print("종료 합니다.")
#         break
#     for el in inp_total_str:
#         if el.isupper():
#             print(el, end='')
#     print()

# upper_str = ""
# for e in input():
#     if e.isupper(): upper_str += e
# print(upper_str)

print(*filter(str.isupper, input()), sep='')
list = ['1', '2', '3']
print(*list, sep='\n')

# def test_arg(arg):
#     if arg:
#         for i in arg:
#             return i
#     else:
#         return

# print(test_arg(list))
