# 문자열 인덱싱 및 슬라이싱
print("'VS code install complete'")
print("C:\\root\\home\\target")
str_a = 'python is very powerful'
print(str_a[:6])
print(str_a[-3:])
# 실행 단축키 -> ctrl + F5
print()

# 리스트 추가 및 길이 확인
list_col = ["red", "blue", "black"]
print(len(list_col))
list_col.append("white")
print(len(list_col))
print(list_col)
list_col.insert(1, "green") # 위치 정해서 추가 가능
print(list_col)
print()

# 만약 append 이외에 방법으로 추가할 경우 생기는 일
list_col += ["red"]
list_col += "red"
# 위 처럼 추가하지 말고 무조건 append 사용
print(list_col)
print(list_col.count("red"))
print(list_col.index("black"))
list_col.remove("blue")
print(list_col)
print()

# set 자료형 -> 중복 허용 안되고 순서 없음
a = {1,2,3,3,1}
print(a,"\n",type(a))
b = {3,4,5,4}
print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a.difference(b)) # 차집합
print()

#  tuple을 쓰는 경우
#  1) 함수에서 하나 이상의 값을 리턴하는 경우
def calc(a,b):
    return a+b, a*b
#  2) 문자열 포맷팅
#  3) 튜플에 있는 값을 함수 인자로 사용하는 경우
print("id:%s, name:%s" %("kim","홍길동"))
print(*calc(3,4)) # 여기서 *는 튜플을 의미한다
print(calc(3,4))
args = (5,6)
print(calc(*args)) # 해당 내용 질문
print(calc(5, 6))
print(*args)
print()

# 형식 변환 방법
print(type((1,2,3)))
print(type(set((1,2,3))))
print()

# dictionary -> {key:value}
# 활용 함수
# 1) dict.items() -> 키와 값을 뽑아줌
# 2) dict.keys() or dict.values()
dict_a = {"banana":"yellow", "apple": "red", "cherry":"red"}
for dic in dict_a.items():
    print(dic)


numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers
print(rest)
print(type(rest))
print()

# *가 하나면 tuple이 됨
def print_numbers(*args):
    print("args -> ", args)
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4, 5)
print()
print()

# *가 두개면 dictionary가 됨
def print_info(**kwargs):
    print("kwargs ->", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name='John', age=25, city='New York')
print()