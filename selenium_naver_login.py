from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard, time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://nid.naver.com/nidlogin.login')

# 아이디 / 비번 입력
login_id = "아이디"
clipboard.copy(login_id)
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL, 'v')
login_pw = "비번"
clipboard.copy(login_pw)
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()

while True:
    pass 