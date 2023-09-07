# Date : 2023-09-06
# Author : J.H.Hwang
# Purpose :  홈페이지 비밀번호를 자동으로 생성하는 프로그램입니다.
# ------------------------------------------------
# 각 사이트 비밀번호 만들기
# 규칙1 : http://naver.com에서 앞의 http:// 잘라내기
# 규칙2 : 처음 만나는 점(.) 이후는 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'o' 갯수 +글자에 포함된 'k' 갯수+ '!' + 자신의이니셜(예: 'jks')

# =========================== 내가 푼 것 ===============================
# source_url = "http://naver.com"
# find_str = "http://"
# tmp_split = source_url.split(".")
# find_result = tmp_split[0].find(find_str)
# if find_result != -1:
#     my_initial = input("자신의 이니셜을 넣어주세요 : ")
#     front_url = tmp_split[0][:len(find_str)]
#     other_url = tmp_split[0][len(find_str):]
#     front_three = other_url[:3]
#     str_len = str(len(other_url))
#     count_o = str(other_url.count("o"))
#     count_k = str(other_url.count("k"))
#     print(f"{front_three}{str_len}{count_o}{count_k}!{my_initial}")
# else:
#     print(f"{find_str}가 없습니다.")

# =========================== 강사 님이 푼 것 ===============================
file_name = "password.txt"
fd = open(file_name, "wt")
while True:
    url = input("사이트 : ")
    if url == 'exit': break
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")] # 슬라이싱 : 처음부터 "." 인덱스 미만
    password = (my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k"))
                + "!" + "hjh")
    print("비밀번호 : " + password)
    fd.write(password + "\n")
fd.close()

