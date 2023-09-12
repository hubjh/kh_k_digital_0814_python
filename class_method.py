# 클래스 메서드 : 클래스 메서드는 클래스 변수를 사용하기 위한 함수 입니다.
# 클래스 메서드는 첫 번째 인자로 클래스를 넘겨 받는 cls가 필요하며 이를 이용해 클래스 변수에 접근
class Person:
    count = 0       # 클래스 변수
    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print(f"{cls.count}명 생성되었습니다.")

james = Person()
maria = Person()

Person.print_count()