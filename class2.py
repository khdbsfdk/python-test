# class 상속 : 부모 class의 모든 속성을 자식 class에게 물려줄 수 있다
# 장점 -> 코드 수를 줄일 수 있고, 매서드 재정의가 가능함
# 부모 class 정의
class Person_parents:
    def __init__(self, name, phoneNum):
        self.name = name
        self.phoneNum = phoneNum
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNum))
    def working(self):
        print("작업 중")
    def sleeping(self):
        print("휴식 중")

# 자식 class 정의
class Student(Person_parents):
    # 부모 매서드 불러오기
    def __init__(self, name, phoneNum, subject, studentID):
        Person_parents.__init__(self, name, phoneNum)
        # 매서드 재정의
        self.subject = subject
        self.studentID = studentID
    # 함수 추가 정의
    def printInfo(self):
        print("학생 이름:{0}, 전화번호:{1}".format(self.name, self.phoneNum))
        print(f"학과:{self.subject}, 학번:{self.studentID}")
        
p = Person_parents("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()