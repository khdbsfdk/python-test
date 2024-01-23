# 가변 인자를 처리하는 함수
def union(*ar): # 중복 인자를 제거하는 함수
    result = []
    print("ar ->", ar, type(ar))
    for item in ar:
        print("item", type(item), item)
        for x in item:
            print("x", type(x), x)
            if x not in result:
                result.append(x)
    return result
print(union('HAM', 'EGG'),"\n")

# 필수 입력과 옵션 입력이 있는 경우
# 딕셔너리 형태를 사용
def userUrlBuilder(server, port, **user):
    str_url = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        str_url += key + "=" + user[key] + "&"
    return str_url
# 주의 사항 - 필수 인자는 앞에, 가변 인자는 뒤에 적어야 혼란이 없다
print(userUrlBuilder("Ycampus.com", "80"))
print(userUrlBuilder("Ycampus.com", "80", id="kis", name="ins"),"\n")

# 람다 함수
# 이름이 없고 함수 객체만 존재하는 익명 함수를 만들 수 있음
# lambda <인자> : <구문>
g = (lambda x,y:x+y)
print(g(3,4))
print( (lambda x:x*2)(3) )
print(globals(),"\n") # g로 정의한 람다 함수는 메모리에 있지만 print만 한 람다는 메모리에 없음

# 필터링 함수
def getBiggerThan20(num):
    return num > 20

list_a = [10, 25, 40]
# 파이썬은 참조가 전달된다!
# filter 사용법 -> filter(조건 함수, 순회 가능한 데이터)
# 해당 함수는 조건에 참인 값을 돌려준다
item_f = filter(getBiggerThan20, list_a)
for i in item_f:
    print(i)
# 이걸 람다 함수로 최적화 하자
item_f = filter(lambda x:x>20, list_a)
print("item_f", item_f)
for i in item_f:
    print(i)
print()


