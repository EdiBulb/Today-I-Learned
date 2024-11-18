import requests
from bs4 import BeautifulSoup

# 1. 웹 페이지 요청(HTML 코드 가져오기)
url = "https://example.com"
response = requests.get(url)
html = response.text # HTML 코드 추출함

# 2. HTML 데이터 파싱

soup = BeautifulSoup(html, "html.parser") # HTML 을 파싱 

# 3. 데이터 추출
title = soup.find("h1").text
print("제목:", title)