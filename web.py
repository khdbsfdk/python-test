# 웹 크롤링 작업
from bs4 import BeautifulSoup

# 페이지 불러오기
page = open(r"C:\Users\PC\Desktop\에티버스\에티러닝\240122_파이썬 교육\works\test01.html",
            "rt", encoding="utf-8").read()

#검색이 용이한 객체 선언
soup = BeautifulSoup(page, "html.parser")

# 전체 문서 보기
# print(soup.prettify())
# <p> 전체를 검색
# print(soup.find_all("p"))
# <p> 하나만 검색
# print(soup.find("p"))
# <p calss='outer-text'> 조건 추가
# print(soup.find_all("p", class_="outer-text"))
# 최근 방법 -> attrs 속성(Attributes)
# print(soup.find_all("p", attrs={"class":"outer-text"}))

# 태그 안쪽에 컨텐츠만 가져오기 -> .text
for tag in soup.find_all("p"):
    title = tag.text.strip()
    print(title)