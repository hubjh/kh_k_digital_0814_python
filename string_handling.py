# 인덱싱과 슬라이싱

jumin = "901120-1234567"

gender = jumin[7]   # 성별
year = jumin[:2]    # 출생
mon = jumin[2:4]    # 월, 2 ~ 4 인덱스
day = jumin[4:6]    # 일, 4 ~ 6 인덱스

print(f"생년월일 : {jumin[:6]}")
print(f"주민번호 뒷자리 : {jumin[7:]}")
print(f"주민번호 뒷자리 : {jumin[-7:]}")
