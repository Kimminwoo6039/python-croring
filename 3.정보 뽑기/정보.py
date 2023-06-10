from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://daum.net'
driver.get(url)

html = driver.page_source

#print(html)


# BeautifulSoup 은 html 뿐만아니라다은언ㅇㅓ형태도 읽읈후 있음.
# html parser 로 읽을게
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
#print(soup)
#type(soup)

# 원하는태그찾을때는 soup.select()
#<a href="https://shoppinghow.kakao.com/top" target="_blank" class="link_recom #txt">쇼핑 홈</a>


# 원하는태그찾을때는 soup.select('태그조건')
# 원하는클래스찾을때는 soup.select('.class속성')
# 원하는id찾을때는 soup.select('#id속성')
# 원하는여러가지 soup.select('h3.link_login')  - > 태그명이 h3 이면서 클래스값이 link_login 값을찾아줘 가능.
# 원하는여러가지 soup.select('부모태그정보 > 자식태그정보')  - > 태그명이 h3 이면서 클래스값이 link_login 값을찾아줘 가능.

# 태그조건
#select = soup.select('h3') # 태그명이 h3 인걸 모두 찾아줘
#print(select)
#print(len(select)) # 태그명이 h3 인것의 개수

# 클래스 조건
# select = soup.select('.link_login') # class 속성은 앞에 .  붙혀줘야함
# print(select)
# print(len(select))

# id 조건

# select = soup.select('h2#kakaotvTitle')
# print(select)

# 부모태그 아래있는 h2

select = soup.select('div > h2.screen_out')[0]
print(select)
print(len(select))