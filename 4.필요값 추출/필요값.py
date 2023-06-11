from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://daum.net'
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

# [리스트 형태로 뽑힘.]
select = soup.select('div > h2.screen_out')[1]
print(select)
print(len(select))

# [ TEXT 만 뽑을때 ]
# <태그>홍길동</태그>
# soup.select('태그')[0].text

text = select.text
print(text)

soup_select = soup.select('.head_bnr > a > img')

# 해당 추출값
print(soup_select)
# JSON 으로 { } 나옴
#print(soup_select[0].attrs)
####################################
# KEY 값으로 값 추출
#print(soup_select[0].attrs.get('src'))
print(soup_select[0]['alt'])
#####################################
print(soup_select[0].attrs.get('alt'))
