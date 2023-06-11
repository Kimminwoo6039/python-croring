from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':

    query = input('검색할 키워드를 입력하세요: ')

    driver = webdriver.Chrome()
    url = 'https://www.naver.com'
    driver.get(url)
    time.sleep(3)

    search_box = driver.find_element(By.ID,"query")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)
    current_url = driver.current_url
    print(current_url)

    search_button = driver.find_element(By.CLASS_NAME , "sc_page_inner")
    element = search_button.find_element(By.TAG_NAME, "a")
    print(element.text)
