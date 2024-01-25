# web server 요청
import requests
# crawling
from bs4 import BeautifulSoup

# web 주소
url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

# 검색이 용이한 객체 선언
soup = BeautifulSoup(response.text, "html.parser")

# 파일 저장
f = open("daangn.txt", "wt", encoding="utf-8")

# 검색
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    title_elem = post.find("h2", attrs={"class":"card-title"})
    price_elem = post.find("div", attrs={"class":"card-price"})
    addr_elem = post.find("div", attrs={"class":"card-region-name"})
    # 여려 줄로 나오는 결과를 가공해보자
    title = title_elem.text.strip().replace("\n", "")
    price = price_elem.text.strip().replace("\n", "")
    addr = addr_elem.text.strip().replace("\n", "")
    # 결과 표시
    print("="*30)
    print(f"상품명 : {title}\n상품 가격 : {price}\n지역 : {addr}")
    print("="*30,"\n")
    # 파일에 쓰기
    f.write("="*30)
    f.write(f"\n상품명 : {title}\n상품 가격 : {price}\n지역 : {addr}\n")
    f.write("="*30)
    f.write("\n")
f.close()