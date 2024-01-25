# 정규표현식이란 특정한 규칙을 가진 문자열을 표현하는데 사용되는 형식 언어
import re

# 특정한 패턴을 검색
result = re.search("[0-9]*", "3575th")
print(result)
print(result.group()) # 찾은 결과만 출력하기
print()
# 얘는 정확하게 일치하는 패턴만
result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())
print()

# \d digit 숫자가 연속으로 4자리
result = re.search("\d{4}", "올해는 2024년 청룡의 해 입니다.")
print(result.group())
