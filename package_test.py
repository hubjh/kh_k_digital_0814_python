from test_package import test_module

name = input("이름을 입력하세요 : ")
greeting = test_module.greeting(name)
print(greeting)