import selenium
from selenium import webdriver

# 현재 크롬 이구 사파리,오페라 등등 있음
driver = webdriver.Chrome()

# 크롬으로 열 url 주소를 넣어주세요.
url ='https://serverrefository.tistory.com/'
driver.get(url)