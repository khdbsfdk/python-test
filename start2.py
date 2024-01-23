# 조건문
# score = int(input("점수를 입력하세요 -> "))

# if 90 <= score <= 100:
#     grade = 'a'
# elif 80 <= score < 90:
#     grade = 'b'
# elif 70 <= score < 80:
#     grade = 'c'
# else:
#     grade = 'd'
# print("내 등급은? -> ", grade)

# continue 사용
list_b  = list(range(1, 11))
for item in list_b:
    if item%2==0:
        continue
    print("Item:{}".format(item))
print()

# 리스트 함축
# <표현식> for <아이템> in <시퀀스 타입 객체> if <조건식>
list_a = [i**2 for i in range(1, 11) if i%2==0]
print(list_a,"\n")
# 복잡한 구조는 그냥 원래대로 짜자 -> 속도차이 없음