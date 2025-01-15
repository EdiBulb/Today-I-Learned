import requests
import csv
from bs4 import BeautifulSoup

# 1. 웹페이지 요청
url = "http://books.toscrape.com/"
response = requests.get(url)
html = response.text

# 2. HTML 데이터 파싱
soup = BeautifulSoup(html, "html.parser")

# 3. 책 제목, 가격, 재고 상태 추출
for book in soup.select(".product_pod"): # product_pod 클래스의 모든 HTML 요소를 선택한다.
    title = book.h3.a["title"] # 책 제목
    price = book.select_one(".price_color").text # 가격
    availability = book.select_one(".instock").text.strip() 
    rating = book.select_one(".star-rating")["class"][1]

    print("제목:", title)
    print("가격:", price)
    print("재고 상태 : ", availability)
    print("별점: ", rating)
    print()

with open("books.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["제목", "가격", "재고 상태"])
    for book in soup.select(".product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        availability = book.select_one(".instock").text.strip()
        writer.writerow([title, price, availability])