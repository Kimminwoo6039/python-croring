
# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json

query = input('검색할 키워드를 입력하세요: ')
start = input('검색할 번호를 입력하세요: ')

client_id = "lxsjpmXAlmJDbhwogAxI"
client_secret = "Ldbi14O1xW"


#searchApis = ['blog','news','book','adult','cafearticle','kin','webkr','image','shop','doc']
searchApis = ['blog']

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
        print(response_body.decode('utf-8'))
        decode = response_body.decode('utf-8')

    else:
        print("Error Code:" + rescode)