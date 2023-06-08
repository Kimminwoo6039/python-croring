from selenium import webdriver


#
# 2 . html 뽑아보기
#

# 2-1
# 드라이버 연결 크롬
driver = webdriver.Chrome()

# 2-2
# url 주소
url ='https://serverrefository.tistory.com/'
driver.get(url)

# 2-3
# url 주소페이지 html 소스코드
# html 코드 잔뜩 나옴
html = driver.page_source


# 1. <태그명> </태그명>  = > <element> <요소>

# 2. <태그명>
#    <태그명 속성1 = 값>
#    <태그명 속성1 = 값 속성2 = 값>

# 3. <태그>홍길동</태그>

# 4.<태그1>  = > 부모태그 (태그1)         부모태그
#     <태그2>   = > 자식태그 (태그2)
#       <태그3>                          자손태크
#       </태그3>
#     </태그2>
#   </태그1>
