# # 계좌 개설
# def open_account(name):
#     print(f"{name}님의 계좌가 개설 되었습니다.")
#     return name     ##  반환 값으로 이름을 전달
#
# # 입금 함수
# def deposit(input):    # 잔고와 입금액을 매개변수로 전달 받음
#     balance += input
#     print(f"{input}이 입금 되었습니다. 잔액은 {balance} 입니다.")
#
# # 출금 함수
# def withdraw(output):
#     if balance >= output:
#         balance -= output
#         print(f"{output}이 출금되었습니다. 잔액은 {balance} 입니다.")
#     else:
#         print(f"출금이 실패 했습니다. 잔액은 {balance} 입니다.")
#
# balance = 0     # 외부에서 선언했지만 매개변수로 전달하여 결과를 리턴 받음
# name = open_account("곰돌이사육사")
# deposit(1000)
# withdraw(500)
# print(f"{name}의 잔액은 {balance} 입니다.")
#

# 계좌 개설
def open_account(name):
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name     ##  반환 값으로 이름을 전달

# 입금 함수
def deposit(input):    # 잔고와 입금액을 매개변수로 전달 받음
    balance[0] += input
    print(f"{input}이 입금 되었습니다. 잔액은 {balance[0]} 입니다.")

# 출금 함수
def withdraw(output):
    if balance[0] >= output:
        balance[0] -= output
        print(f"{output}이 출금되었습니다. 잔액은 {balance[0]} 입니다.")
    else:
        print(f"출금이 실패 했습니다. 잔액은 {balance[0]} 입니다.")

balance = [0]     # 외부에서 선언했지만 매개변수로 전달하여 결과를 리턴 받음
name = open_account("곰돌이사육사")
deposit(1000)
withdraw(500)
print(f"{name}의 잔액은 {balance[0]} 입니다.")

# 두 코드 모두 계좌 개설, 입금, 출금 등의 기능을 구현하고 있지만, 오류가 나는 이유는 변수 balance의 스코프와 변경 가능성(Mutability)과 관련이 있습니다.
#
# 첫 번째 코드에서는 balance 변수를 함수 내에서 수정하려고 하지만, deposit 및 withdraw 함수에서 balance 변수를 수정할 때 Python은 이 변수가 함수 내부에서 로컬 변수로 간주하고 있기 때문에 오류가 발생합니다.
#
# 두 번째 코드에서는 balance 변수를 리스트로 만들어 전달하고 있습니다. 이렇게 하면 deposit 및 withdraw 함수에서 balance[0]을 수정할 수 있습니다. 리스트는 변경 가능한(Mutable) 데이터 유형이므로 함수 내에서 수정이 가능합니다.
#
# 따라서 두 번째 코드에서는 balance 변수를 리스트로 만들어서 함수에 전달하고, 함수 내에서는 리스트의 요소를 수정하는 방식으로 잔고를 변경하고 있습니다. 이것이 오류가 발생하지 않는 이유입니다.
#
# 첫 번째 코드에서 오류를 수정하려면 deposit 및 withdraw 함수에서 balance 변수를 전역 변수로 선언하고, 함수 내에서 global 키워드를 사용하여 전역 변수임을 명시적으로 지정해야 합니다.
#
# 그러나 전역 변수를 사용하는 것은 보통 권장되지 않으며, 코드의 가독성과 유지 관리성을 저하시킬 수 있으므로 가능하면 두 번째 코드와 같이 매개변수를 통해 값을 전달하는 방식을 사용하는 것이 더 좋습니다.