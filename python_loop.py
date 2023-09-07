# 반복문 : 조건이 참인 동안 계속 수행되는 구문
# n = int(input("정수를 입력 하세요 : "))
# sum = 0
# while n:    # python은 정수값이 0이 아니면 참으로 간주
#     sum += n
#     n -= 1  # python은 증감 연산자가 없음
# print(sum)

# while True:
#     age = int(input("나이를 입력 하세요 : "))
#     if 0 < age < 200: break
#     print("나이 입력 범위가 벗어 났습니다.")

# for 요소 in 시퀀스: 시퀀스의 각 요소를 순회하는데 사용 (Java의 향상된 for문과 동일)
# fruits = ["apple", "banana", "cherry", ["seoul", "korea"]]
# print(fruits[3][1][0])
# for e in fruits:
#     print(e[0])
#
# str1 = "서울시 강남구 역삼동 KH정보교육원"
# for e in str1:
#     print(e, end="/")

# // for(int i = 0; i < 100; i++) {}

# for 변수 in range(시작값, 종료값, 증감값):
# n = int(input("정수를 입력 하세요 : "))
# sum = 0
# for i in range(1, n+1): # 1부터 n+1 미만
#     sum += i
# print(sum)

# for 문을 역순으로 반복하기
# for i in range(10, -1, -2):     # 10 ~ 0 까지 출력
#     print(i)

# 이중 for문
# n = int(input("정수를 입력 하세요 : "))
# for i in range(0, n):
#     for j in range(0, n):
#         print("*", end=" ")
#     print()

# 구구단 찍기
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i * j}")
#     print()

# 홀수/짝수 나누어 찍기
# n = int(input("정수 입력 : "))
# for i in range(0, n):
#     for j in range(0, n):
#         if j % 2 == 0: print("$", end=" ")
#         else: print("*", end=" ")
#     print()

# 사각형 찍기
# 정수값을 n을 입력 받아 n * n 크기의 행렬을 출력하는 프로그램 작성
# 값은 1부터 시작

# n = int(input("정수 입력 : "))
# for i in range(1, n * n + 1):
#     print(f"{i:>3}", end =" ")
#     if i % n == 0:
#         print()


# n = int(input("가운데가 빈사각형으로 별찍기 : "))
# for i in range(0, n):
#     for j in range(0, n):
#         if (0 < j < n - 1 and 0 < i < n - 1):
#             print(end="  ")
#         else:
#             print("*", end=" ")
#     print()

# n = int(input("삼각형으로 별찍기 : "))
# for i in range(0, n):
#     for j in range(0, n):
#         if(i >= j):
#             print("*", end=" ")
#     print()

# n = int(input("삼각형 : "))
# for i in range(n):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# n = int(input("뒤집힌 삼각형1 : "))
# for i in range(n):
#     for j in range(n - i):
#         print("*", end=" ")
#     print()

# n = int(input("아래로 뾰족한 삼각형 : "))
# for i in range(n):
#     print(" " * i, end="")
#     for j in range(n - i):
#         print("*", end=" ")
#     print()


# n = int(input("둔각 삼각형 : "))
# for i in range(n):
#     print(" " * i, end="")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()


# n = int(input("위로 뾰족한 삼각형 : "))
# for i in range(n):
#     print(" " * (n - i), end="")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()