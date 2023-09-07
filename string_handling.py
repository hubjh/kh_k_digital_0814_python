# Date : 2023-09-06
# Author : J.H.Hwang
# Purpose :  문자열처리를 연습하는 프로그램입니다.
# ------------------------------------------------
# 인덱싱과 슬라이싱

jumin = "901120-1234567"

gender = jumin[7]   # 성별
year = jumin[:2]    # 출생
mon = jumin[2:4]    # 월, 2 ~ 4 인덱스
day = jumin[4:6]    # 일, 4 ~ 6 인덱스

print(f"생년월일 : {jumin[:6]}")
print(f"주민번호 뒷자리 : {jumin[7:]}")
print(f"주민번호 뒷자리 : {jumin[-7:]}")   # 맨 뒷자리가 -1

if gender == "1":
    print("남성입니다.")
else:
    print("여성입니다.")

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
# a[1] = "L" # 문자열의 요소는 읽을 수는 있지만 변경은 되지 않음. 리터럴 상수

# 대소문자 바꾸기
aa = "Hello Python Program...."
bb = aa.upper()
print(bb)
print(aa.lower())

# 문자열 변경 : replace("")
input_str = "Hello Python Program...."
new_str = input_str.replace("Python", "JavaScript")
# new_str = input_str.replace("Python","")
print(new_str)

# 문자열에 포함된 문자 갯수 세기, 길이 확인
print(len(input_str))           # 문자열의 길이를 반환, 별도의 외부(범용) 함수(메서드)를 사용하는 방식
print(input_str.count("lo"))   # 문자열에서 포함된 문자(열)의 갯수를 반환

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"길이 {len(test)}")
print(test.__len__())
print(input_str.__len__())      # 문자열에 포함된 내장 함수(메서드)

# 문자열 찾기 : find(), rfind(), index()
# find() : 찾은 문자열의 첫 번째 인덱스를 반환, 못찾으면 -1 반환
# index() : 찾은 문자열의 첫 번째 인덱스를 반환, 못찾으면 ValueError 예외 발생

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"))   # 뒤에서 부터 찾지만 위치에 대한 인덱스는 앞에서 부터 계산
print(phrase[34:36])
print(phrase.index("포기"))
print(phrase.find("나에게"))   # 못 찾으면 -1
# print(phrase.index("나에게"))  # 못 찾으면 ValueError 예외 발생

new_phrase = phrase.replace("가장", "나에게")
print(new_phrase)

print("태양고" + "나희도") # 가능
# print("태양고" + 2) # 문자열과 정수의 연산 불가능
print("안녕하세요" * 3)  ## 해당 문자열을 수 만큼 반복 수행
print("안녕하세요", "!" * 5, "\n", "\t", "=" * 3, "태양고", "=" * 3, "\n나희도" * 3, "입니다.")

# 문자열 앞/뒤 공백 제거 : strip()
input_aa = """
    안녕하세요.
문자열 함수를 알아 봅시다.


"""

print(input_aa.strip())
