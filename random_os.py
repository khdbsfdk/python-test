import random
# import os.path
from os.path import *
import glob
from os import *

print(random.random()) # 0 ~ 1 사이의 실수 무작위
print(random.random())
print([random.randrange(20) for i in range(10)]) # 0 ~ 19 중에 중복 허용으로 무작위 숫자
print([random.randrange(20) for i in range(10)],"\n")

# 유니크 샘플 생성(중복 허용 X)
print(random.sample(range(20), 10),"\n")

# 로또 버노 마냥 출력해보자
lotto = list(range(1, 46))
random.shuffle(lotto)
print(random.sample(lotto, 6),"\n")

# 파일 다루기
print(abspath("python.exe")) # 절대 경로로 변환
print(basename("C:\\ProgramData\\Anaconda3\\python.exe")) # 경로 빼고 파일 이름만

f_name = "C:\\ProgramData\\Anaconda3\\python.exe"
if exists(f_name):
    print("파일 크기:{}".format(getsize(f_name)))
else:
    print("파일 없음")
print()


# OS 모듈
print("OS name :", name)
print("envirment :", environ)
# system("notepad.exe")
print()

print(glob.glob("*.py"), type(glob.glob("*.py")))
print()

