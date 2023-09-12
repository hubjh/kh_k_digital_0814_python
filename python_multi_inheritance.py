# 다중 상속이란? 여러 부모로 부터 상속을 받는 것 ( 자바에서는 하나의 상속, 나머지는 인터페이스, 다이아몬드 상속 문제 )
class Person :
    def __init__(self, eat):
        self.eat = eat
        print("인간 입니다.")
    def set_eat(self):
        print(f"{self.eat} 밥을 먹습니다.")

class Student(Person):
    def __init__(self, eat, study):
        Person.__init__(self, eat)
        self.study = study
        print("학생 입니다.")
    def set_study(self, study):
        self.study = study
        print("공부 합니다.")

class Worker(Person):
    def __init__(self, eat, work):
        Person.__init__(self, eat)
        self.work = work
        print("직장인 입니다.")
    def set_work(self, work):
        self.work = work
        print("일 합니다.")

class Developer(Student, Worker):
    def __init__ (self, eat, study, work):
        Student.__init__(self, eat, study)
        Worker.__init__(self, eat, work)
        print("개발자 입니다.")

dev = Developer(1, 1, 1)
dev.eat = 200
dev.set_eat()