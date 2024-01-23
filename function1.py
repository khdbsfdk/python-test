# 함수는 객체처럼 메모리 상에 생성된다.
# def <함수명>(인자 혹은 파라미터 여러개):
#     <구문>
#     return <반환값>

def test_func():
    return None
print(id(test_func()),"\n")

def setValue(val):
    # 지역변수 초기화
    x = val
    print("함수 내부 지역번수 x :", x)
# 함수 호출
retValue = setValue(5)
print(retValue,"\n")

def swap(x, y):
    return y, x

retValue = swap(3, 4)
print(retValue)
a, b = swap(3, 4)
print(a, b,"\n")


def func(*arg):
    global o
    for i in arg:
        print(i)
    o = i
print(func(1, 2))
print(o,"\n")

# 사용하는 함수 내부에서 변수가 없다면 전역 영역에서 변수를 찾아씀(LGB)
x = 1
def func_bun(a):
    return a + x
print(func_bun(4),"\n")

# 기본 값이 정해진 함수(값이 들어오지 않아도 오류 안남 -> 필수가 아니다!)
def func_add(a=10, b=20):
    return a+b
print(func_add())
print(func_add(1))
print(func_add(5, 5),"\n")

# 함수 입력 시 매개변수 전달(키워드 )
def ConnectURL(server, port):
    str_url = "https://" + server + "::" + port
    return str_url
print(ConnectURL("8080", "192.168.100.105"))
print(ConnectURL(port="8080", server="192.168.100.105"),"\n")