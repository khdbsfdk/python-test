for i in range(1, 10):
    str_url = "https://www.ycampus.com/?page=" + str(i)
    print("url -> ", str_url)
print()

# 왼쪽 정렬
for x in range(1, 6):
    print("{} * {} = {}".format(x, x, str(x*x)))
print()

# 문자열 오른쪽 정렬 -> rjust()
for i in range(1, 10):
    print("{} * {} = {}".format(i, i, str(i*i).rjust(3)))
print()

# 0으로 채우기
for x in range(1, 6):
    print(x, "8", x, "=", str(x*x).zfill(10))
print()

# 서식 지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3)) # 실수 표기
print("{0:.2f}".format(4/3)) # 소수점 2자리 표기
print()