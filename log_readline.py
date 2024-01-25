import re

f = open('PV3.txt', 'rt')
g = open('PV3_copy.txt', 'wt', encoding='utf-8')

# line = f.readline()
# while (line != ''): # EOF가 아니면
#     if (re.search("ERROR", line)):
#         g.write(line + '\n')
#     line = f.readline()

line = f.readline()
while (line != ''): # EOF가 아니면
    if re.search("error", line.lower()):  # 대소문자 구분 없이 하려면 line을 다 소문자로 바꿔서 찾자
        g.write(line + '\n')
    line = f.readline()

f.close()
g.close()