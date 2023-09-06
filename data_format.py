# 값을 할당 하는 방법
a = b = c = 1
print(a, b, c)

a, b, c = 1, False, "곰돌이사육사"  # 여러 개의 변수를 한번에 대입,
print(a, b, c)

# 타입 확인
# age = int(input("나이를 입력 하세요 : "))
# print(type(age))

# value = 0o77
value = 0xFFFFFFFF
print(value)

# boolean type : 참과 거짓의 값을 가짐
print(bool(1))  # True
print(bool(0))  # False
print(bool(-100))  # True
print(bool(""))  # False
print(bool(None))  # 값이 정해 지지 않았음을 의미, False

# string type :
str1 = "Hello Python!!!!"
print(str1)
print(str1[0])   # 인덱싱
print(str1[2:5]) # 2번 인덱스에서 5번 인덱스 미만  :  llo
print(str1[2:])
print(str1[:-4])
print(str1 * 3)
print(str1 + "TEST")

# 형변환 : 파이썬은 값이 할당되는 순간 형이 결정됨, 이 후 데이터형을 변경하고자 할 때 형변환을 사용
print(10 + int("10"))
print("나이 : " + str(30))
aa = 10
print(int(1 + 3.141592))
print(1 + 3.141592 + float("4.44"))
print(type(1 + 3.141592 + float("4.44")))
