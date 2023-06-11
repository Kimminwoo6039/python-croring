from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd



Id = input('인스타그램 아이디 입력해주세요 : ')
pw = input('인스타그램 비밀번호 입력해주세요 : ')
search = input('인스타그램 검색할 키워드를 작성해주세요 : ')

# 크롬 연결
driver = webdriver.Chrome()
url = 'https://www.instagram.com/'
driver.get(url)

# 3초까지 대기
time.sleep(3)

# 로그인 하기 ( 아아디,비밀번호 입력 )
search_box = driver.find_element(By.NAME, "username")
search_box.send_keys(Id)

search_box = driver.find_element(By.NAME, "password")
search_box.send_keys(pw)
search_box.send_keys(Keys.RETURN)
time.sleep(6)

# 조회할 키워드 입력
url = f"https://www.instagram.com/explore/tags/{search}"
driver.get(url)

# 첫번째 게시물 클릭
time.sleep(6)
first_div = driver.find_elements(By.CSS_SELECTOR, 'div._aagw')[0]
first_div.click()

# 다음 게시물 클릭
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR, 'button._abl-')
element.click()

# 데이터 수집개수
total = 15

# 전체 게시글 정보 저장할 객체
results = []

# 반복 수집
for i in range(total):

# 2.게시물 데이터 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    contentAll = soup.select('div._a9zs')
    content = contentAll[0].text
    print(contentAll[1:])
# 좋아요 개수
#     try:
#         heartInt = soup.select('span> a > span')[0].text.replace('좋아요 ','').replace('개','')
#     except ValueError:
#         heartInt = '0'
#     print(heartInt)
# 작성일
    datetime = soup.select('time._a9ze')[0]['datetime'][:10]
    print(datetime)

# 게시글 1개 정보 저장
    data = [content,datetime]
    results.append(data)

# 3.다음페이지
    element1 = driver.find_elements(By.CSS_SELECTOR, 'button._abl-')[1]
    element1.click()
    time.sleep(3)

pd = pd.DataFrame(results)
pd.columns = ['content','날짜']
pd.to_excel('./인스타그램.xlsx', index=False)
