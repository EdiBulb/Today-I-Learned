import requests
from bs4 import BeautifulSoup
import time
time.sleep(1)  # 1초 대기


# 1. 웹 페이지 요청
url = "http://quotes.toscrape.com/"
response = requests.get(url) # 웹 페이지 요청
html = response.text # HTML 코드 추출

# 2. HTML 데이터 파싱
soup = BeautifulSoup(html, "html.parser")

# 3. 뉴스 제목과 링크 추출
for quote in soup.select(".quote"):
    text = quote.select_one(".text").text
    author = quote.select_one(".author").text
    print("명언:", text)
    print("저자:", author)
    print("-"* 80)
