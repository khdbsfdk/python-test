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