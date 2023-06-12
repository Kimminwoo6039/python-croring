from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd


Id = input('페이스북 아이디 입력해주세요 : ')
pw = input('페이스북 비밀번호 입력해주세요 : ')
search = input('페이스북 검색할 키워드를 작성해주세요 : ')

# 크롬 연결
driver = webdriver.Chrome()
url = 'https://www.facebook.com/'
driver.get(url)

# 3초까지 대기
time.sleep(3)

# 로그인 하기 ( 아아디,비밀번호 입력 )
search_box = driver.find_element(By.ID, "email")
search_box.send_keys(Id)

search_box = driver.find_element(By.ID, "pass")
search_box.send_keys(pw)
search_box.send_keys(Keys.RETURN)
time.sleep(6)

# 조회할 키워드 입력
url = f"https://www.facebook.com/search/top?q={search}"
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

find = soup.find("div", {"aria-label": "검색 결과"})
print(find)