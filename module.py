from DemoSet import union
import numpy, sys
print()
print(dir())
print(union([1,2,3],[3,4,5]),"\n")
# from <모듈이름> import <함수>를 사용한다는건 모듈을 생략하고 함수만 쓰겠다는 것.
# 원래 정석은 import DemoSet 후 DemoDet.union이 맞음

# from <모듈> import * 을 쓰면 모듈 명 빼고 함수 전체를 쓰겠다는 것.
# 여기서 *은 와일드카드라고 한다. 그래서 모듈의 전역 공간(메모리)는 할당 되지 않는다.
from DemoSet import *
print(dir(),"\n")

# 만약 보안 때문에 소스 파일을 공유 못한다?
# 파이썬은 실행 파일 즉, 컴파일러가 있는데, 이는 Lib > __pycache 디렉토리 내 pyc 형태로 있음
# 이 바이트 코드는 인터프리팅 없이 로딩 되므로 임포트 속도가 빠르다!

# 자 만약 고객에게 실행 파일만 주고 싶다면 cmd에서 pyinstaller --onefile <py파일>를 통해
# exe 파일을 생성하여 줄 수 있음, 그럼 dist 디렉토리 안에 exe 파일이 들어있음

# 모듈을 복사하여 인스턴스를 만들어도 같은 모듈 원본을 바라본다.
import DemoModule as m1
import DemoModule as m2
m1.x = 100 # 모듈 내 변수 수정
m2.printX()

