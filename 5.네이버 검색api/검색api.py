
# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json
from bs4 import BeautifulSoup

query = input('검색할 키워드를 입력하세요: ')
start = input('검색할 번호를 입력하세요: ')


# 네이버 클라이언트 키
client_id = "lxsjpmXAlmJDbhwogAxI"
client_secret = "Ldbi14O1xW"


# 검색 키워드 adult 성인 확인./
#searchApis = ['blog','news','book','cafearticle','kin','webkr','image','shop','doc']
searchApis = ['blog','cafearticle']


# 검색 결과값.
title = ''
link = ''


# 검색 데이터
for searchApi in searchApis :
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/{searchApi}?query=" + encText + "&display=100&start="+start  # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    print(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        decodes = response_body.decode('utf-8')
        print(decodes)
        result = json.loads(decodes)
        soup = BeautifulSoup(decodes,'html.parser')

#타이틀

        for a in result['items']:
            print("title = " + a['title'])
            print("link = " + a['link'])
            print("description = " + a['description'])
            #print("bloggername = " + a['bloggername'])
            #print("bloggerlink = " + a['bloggerlink'])
            # print("postdate = " + a['postdate'])
            title_ = a['title']
            print("다음페이지")

    else:
        print("Error Code:" + rescode)

