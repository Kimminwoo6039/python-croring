import selenium
from selenium import webdriver



# 
#  1 . URL 주소로 사이트 접속하기
#              (크롬)
#

# 1-1
# 현재 크롬 이구 사파리,오페라 등등 있음 
driver = webdriver.Chrome()

# 1-2
# 크롬으로 열 url 주소를 넣어주세요.
url ='https://serverrefository.tistory.com/'
driver.get(url)

# 1-3
# for 문으로 반복문을 돌릴때 (일반적인것)
search = ['파이썬','룰루랄','안녕']
for word in search:
    print(word)
    url = 'https://serverrefository.tistory.com/'

# 1-3 (결과값)    
#파이썬
#https://serverrefository.tistory.com/
#룰루랄
#https://serverrefository.tistory.com/
#안녕
#https://serverrefository.tistory.com/


# 1-4 
# for 문으로 search 값으로 하나씩 대입 할때
# f + 'url={search.index[0]}'

search = ['파이썬','룰루랄','안녕']
for word in search:
    print(word)
    url = f'https://serverrefository.tistory.com/?{word}'
    print(url)

# 1-4     
#파이썬
#https://serverrefository.tistory.com/?파이썬
#룰루랄
#https://serverrefository.tistory.com/?룰루랄
#안녕
#https://serverrefository.tistory.com/?안녕     


