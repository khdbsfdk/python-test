# Form.ui + form.py 가 한 묶음

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import requests
from bs4 import BeautifulSoup

# 디자인 파일 미리 로딩
# form_class = uic.loadUiType("demo_guiTool.ui")[0]
form_class = uic.loadUiType("test_gui.ui")[0]

# form class 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫 번째 QT Demo")
    def firstClick(self):
        self.label.setText("첫 번째 단추 누름")
        # 당근 크롤링 복붙
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        # 파일 저장
        f = open("daangn.txt", "wt", encoding="utf-8")
        # 검색
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            title_elem = post.find("h2", attrs={"class":"card-title"})
            price_elem = post.find("div", attrs={"class":"card-price"})
            addr_elem = post.find("div", attrs={"class":"card-region-name"})
            # 결과를 가공
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
        # 여기까지 복사
    def secondClick(self):
        self.label.setText("두 번째 단추 누름")
    def thirdClick(self):
        self.label.setText("세 번째 단추 누름")

# 모듈 실행 여부 확인 -> 진입점 (Entry Point)
if __name__ == "__main__": # 직접 실행한건지 확인
    # 실행 프로세스
    app = QApplication(sys.argv)
    # 폼 실행
    demo_form = DemoForm()
    # 화면 보여주기
    demo_form.show()
    app.exec_()