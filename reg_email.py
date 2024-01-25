import re

# 대상 텍스트
text = """
예시 텍스트입니다.
이메일 주소 목록:
1. user1@example.com
2. user2@gmail.com
3. user3@yahoo.com
4. user4@hotmail.com
5. user5@example.net
6. user6@gmail.com
7. user7@yahoo.co.kr
8. user8@hotmail.co.uk
9. user9@example.org
10. user10@gmail.co.in
"""

# 이메일 주소를 찾기 위한 정규 표현식 패턴
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# re.findall()을 사용하여 이메일 주소 찾기
email_addresses = re.findall(email_pattern, text)
print(email_addresses)

# 찾은 이메일 주소 출력
if email_addresses:
    print("찾은 이메일 주소 목록:")
    for email in email_addresses:
        print(email)
else:
    print("이메일 주소를 찾을 수 없습니다.")
