from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

Id = input('인스타그램 아이디 입력해주세요 : ')
pw = input('인스타그램 비밀번호 입력해주세요 : ')
search = input('인스타그램 검색할 키워드를 작성해주세요 : ')

driver = webdriver.Chrome()
url = 'https://www.instagram.com/'
driver.get(url)
time.sleep(3)


search_box = driver.find_element(By.NAME, "username")
search_box.send_keys(Id)

search_box = driver.find_element(By.NAME, "password")
search_box.send_keys(pw)
search_box.send_keys(Keys.RETURN)
time.sleep(6)

# 단건으로조회
url = f"https://www.instagram.com/explore/tags/{search}"
driver.get(url)

# # 여러건 조회
# searchList = ['마약','필로폰','중독']
# for searching in searchList:
#     url = f"https://www.instagram.com/explore/tags/{searching}"
#     driver.get(url)

# 첫번째게시물 클릭
time.sleep(15)
first_div = driver.find_elements(By.CSS_SELECTOR, 'div._aagw')[0]
first_div.click()

# # # 다음게시물 클릭
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR, 'button._abl-')
element.click()

time.sleep(3)
##### 게시물정보 수집하기
# html = driver.page_source
# soup = BeautifulSoup(html,'html.parser')
# contentAll = soup.select('div._a9zs')
# content = contentAll[0].text
# print(content)

# 본문찾기

# 좋아요 개수
#heart = soup.select('span> a > span.x193iq5w')[0].text
# heart = soup.select('span> a > span')[0].text[4:-1]
# heart = soup.select('span> a > span')[0].text[4:]
# heartInt = soup.select('span> a > span')[0].text.replace('좋아요 ','').replace('개','')


#
#
# # # 반복해서 10개 게시물 수집
# # 1.첫번째 게시물클릭
for i in range(10):
# 2.게시물 데이터 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    contentAll = soup.select('div._a9zs')
    content = contentAll[0].text
    print(contentAll[1:])

# 3.다음페이지
    element1 = driver.find_elements(By.CSS_SELECTOR, 'button._abl-')[1]
    element1.click()
    time.sleep(3)


# try catch 문
 
# try:
#     like = soup.select().text
#     view = 0
# except: # 만약 에러인경우동영상 
#     view = so