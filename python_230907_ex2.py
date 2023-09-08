# ===================== 회원정보 출력하기 =============================
# name_inp = input("이름 입력 : ")
# while True:
#     age_inp = int(input("나이 입력 (1 ~ 199) : "))
#     if 0 < age_inp < 200:
#         break
#     else:
#         print("나이를 다시 입력해주세요.")
# while True:
#     gender_inp = input("성별 입력 [M] [W]: ")
#     if gender_inp in ['m', 'M', 'w', 'W']:
#         break
#     else:
#         print("성별를 다시 입력해주세요.")
# while True:
#     job_inp = int(input("직업 입력  [1]학생, [2]회사원, [3]주부, [4]무직 : "))
#     if job_inp in range(1, 4):
#         if job_inp == 1:
#             job_info = "학생"
#         if job_inp == 2:
#             job_info = "회사원"
#         if job_inp == 3:
#             job_info = "주부"
#         if job_inp == 4:
#             job_info = "무직"
#         break
#     else:
#         print("직업을 다시 입력해주세요.")
#
# print(f'''이름 : {name_inp}
# 나이 : {age_inp}
# 성별 : {gender_inp}
# 직업 : {job_info}
# ''')


# ======================= 숫자의 개수 ==========================
# while True:
#     a_inp = int(input("a (100 ~ 999) : "))
#     if 100 <= a_inp < 1000:
#         break
#     else:
#         print("숫자 a를 다시 입력해주세요.")
# while True:
#     b_inp = int(input("b (100 ~ 999) : "))
#     if 100 <= b_inp < 1000:
#         break
#     else:
#         print("숫자 b를 다시 입력해주세요.")
# while True:
#     c_inp = int(input("c (100 ~ 999) : "))
#     if 100 <= c_inp < 1000:
#         break
#     else:
#         print("숫자 c를 다시 입력해주세요.")
#
# rst_num = a_inp * b_inp * c_inp
# ls = str(rst_num)
# for i in range(10) :
#     print(f'{str(i)} : {ls.count(str(i))}') # 해당 문자의 개수 반환

# print(f"""result_number : {rst_num}
# 0 : {str(rst_num).count('0')}개
# 1 : {str(rst_num).count('1')}개
# 2 : {str(rst_num).count('2')}개
# 3 : {str(rst_num).count('3')}개
# 4 : {str(rst_num).count('4')}개
# 5 : {str(rst_num).count('5')}개
# 6 : {str(rst_num).count('6')}개
# 7 : {str(rst_num).count('7')}개
# 8 : {str(rst_num).count('8')}개
# 9 : {str(rst_num).count('9')}개
# """)


# ================== 대소문자 바꾸기 ====================
# while True:
#     str_inp = input("String (100 ~ 999) : ")
#     if len(str_inp) <= 100:
#         break
#     else:
#         print("문자열을 다시 입력해주세요.")
# new_str = []
# for el in str_inp:
#     if 65 <= ord(el) <= 91:
#         new_str.append(el.lower())
#     else:
#         new_str.append(el.upper())
# print(''.join(str(s) for s in new_str))



# ==================== 통화 요금 ========================
# call_time_list = []
# while True:
#     call_cnt = int(input("통화의 개수 : "))
#     if 0 < call_cnt <= 20:
#         break
#     else:
#         print("통화 개수를 다시 입력해주세요.")
#
# for i in range(call_cnt):
#     print(f"입력된 통화 시간 수 : {i+1}")
#     while True:
#         call_time = int(input("통화 시간 입력 : "))
#         if 0 < call_time <= 10000:
#             call_time_list.append(call_time)
#             break
#         else:
#             print("통화 시간을 다시 입력 해주세요.")
# while True:
#     yogum = input("요금제 입력 [Y] [M]: ")
#     if yogum in ['y', 'Y', 'm', 'M']:
#         break
#     else:
#         print("요금제를 다시 입력해주세요.")
#
# total_usage = 0
# for clt in call_time_list:
#     if yogum == 'y' or yogum == 'Y':
#         if clt < 30:
#             total_usage += 10
#         else:
#             total_usage += 20
#     if yogum == 'm' or yogum == 'M':
#         if clt < 60:
#             total_usage += 15
#         else:
#             total_usage += 30
#
# print(f"total_usage : {total_usage}")