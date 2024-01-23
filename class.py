# 객체 지향 프로그램의 특징
# 1) 추상성 : 꼭 필요한 부분만 구현하는 것
# 2) 상속성 : 부모 클래스애서 공통 부분을 상속 받는 것
# 3) 다형성 : 동일한 인터페이스에 대해 구체적인 인스턴스마다 다른 동작을 시킴

# 쿠키틀을 class라고 하고 원본 즉, 청사진이라 함
# 인스턴스(object)를 복사본이라 하는데 쿠키틀로 만든 쿠키임
# 다 만들고 매서드 호출하면 끝남

# class 안에는 data + method가 들어있는데
# 데이터는 맴버 변수, 매서드는 맴버 매서드임
# class 클래스이름(상위클래스):
#     내용
    # def __init__(self): -> 이 부분은 초기화 매서드인데,
    # 이 중에 self는 자기 자신임. 첫 번째 인자로 복사본 자신을 의미한다.

class Person:
    def __init__(self):
        # 인스턴스 맴버변수 선언
        self.name = "default name"
    def print(self):
        print(f"my name is {self.name}")

p1 = Person()
p2 = Person()
p2.name = "전우치"
p1.print()
p2.print()
print()


# 전역 변수가 겹치는 경우
str_name = "전역 변수의 값이당"
class DemoString:
    def __init__(self):
        self.str_name = ""
    def set(self, msg):
        self.str_name = msg
    def print(self):
        print(str_name)
        # print(self.str_name)
demostr = DemoString()
demostr.set("message")
demostr.print()
print()
# class 내 변수는 항상 self.을 붙여 이런 실수를 방지하자

# 생성자 및 소멸자 매서드 -> 메모리 해제 등의 종료 작업을 위해 소멸자 메서드 사용가능
# def __del__(self):
# 참고로 __<object__로 시작하는 맴버 변수는 Naming Mangling이라고 외부에서 접근이 불가함

class BankAccount:
    def __init__(self, id, name, balance):
        # self.id = id
        # self.name = name
        # self.balance = balance
        self.__id = id
        self.__name = name
        self.__balance = balance
    def deposit(self, amount):
        # self.balance += amount
        self.__balance += amount
    def withdraw(self, amount):
        # self.balance -= amount
        self.__balance -= amount
    def __str__(self):
        # return "{0} , {1} , {2}".format(self.id, \
        #     self.name, self.balance)
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

# 객체 정의
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000) # 17000
#__로 숨기는 목적은 객체 정의 없이 직접 접근을 막기 위함
account1.balance = 15000000
print(account1)
# __로 숨기더라도 _{클래스명}__{변수}로 조회 가능
print(account1._BankAccount__balance)
account1._BankAccount__balance = 100000
print(account1)
print()
