print("\n",dir(str),"\n")

str_a = "python is very powerful"
str_b = "파이썬은 쉬운 편이지"
print(str_a.capitalize())
print(str_a.count("p"))
print(str_a.count("p", 7))
# 시작 종료 패턴
print(str_a.startswith("py"))
print(str_a.endswith("ful"),"\n")
# 알파벳만 있는지, 숫자만 있는지
print("MBCFFOU".isalnum())
print("MBC:FFOU".isalnum()) # 특수 문자는 안됨
print("7588".isdecimal(),"\n")

# 반복 문구
list_n = ["홍길동", "이순신", "전우치"]
for name in list_n:
    print("="*40)
    print("안녕하세요 {}님, 감기 조심하세요.".format(name))
    print("#"*40)
print()

# 앞/뒤 공백 문자 제거
data = "<<< spam and ham is meat >>>"
print(data)
result_str = data.strip("<> ") # 문자 지정하여 삭제 가능
print(result_str)
result2 = result_str.replace(" ", "")
print(result2,"\n")

# 하나의 문자열로 합치기
result_split = result_str.split() # 공백 기준으로 나눠서 리스트로 바꿔
print(result_split)
print(":) ".join(result_split),"\n") # 공백에 지정 문자열을 넣어


import re 

result = re.search("error", "어떤 문자열 Error".lower())
print(result.group())