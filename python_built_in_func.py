# 내장 함수 : 파이썬이 기본적으로 제공, import가 필요 없음
# 외장 함수 : 파이썬이 기본적으로 제공, import가 필요함.

# 큰 값 작은 값 찾기
# print(max(1,2,3,4,5,6,7,8,9,11))
# print(min(12,2,5,7,8,543,67,8,9))

# 총 합 구하기
# print(sum([1,2,543,6,8,9,3,6677,23]))   # 리스트에 총 합
# print(sum((1,2,543,6,8,9,3,6677,23)))   # 튜플에 대한 총 합
#
# num = list(map(int, input("정수값 입력 : ").split()))
# print(f"입력 받은 수의 총 합 : {sum(num)}")
# print(f"입력 받은 수의 평균 : {sum(num)/len(num)}")

# 몫과 나머지 구하기
# print(f'몫과 나머지 : {divmod(10, 4)}') # 튜플의 동작 원리, 두 개의 반환 값으로 받음

# 여러개의 값을 한번에 입력 받아 리스트로 만들기
# 최대값, 최소값, 합계, 평균
# n = list(map(int, input("정수를 입력 하세요 : ").split()))
# print(f"최대값 : {max(n)}")
# print(f"최소값 : {min(n)}")
# print(f"합계 : {sum(n)}")
# print(f"평균 : {sum(n) / len(n)}")

# 합에 대해서 5로 나누고 몫과 나머지 출력 하는 함수
# print(divmod(sum(n),5))
# print(type(divmod(sum(n),5)))

print(sorted([1,2,543,6,8,9,3,6677,23]))   # 정렬
print(sorted([1,2,543,6,8,9,3,6677,23], reverse=True))   # 역정렬

my_list = [1,2,3,4,5,6,7,8,9,77,2235]
print(my_list.sort())
print(my_list)
print(my_list.sort(reverse=True))
print(my_list)