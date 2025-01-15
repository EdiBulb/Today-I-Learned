import requests
from bs4 import BeautifulSoup

# 타겟 URL
url = "https://www.amazon.com/s?k=MacBook"
headers = {"User-Agent": "Mozilla/5.0"} # 이 코드의 역할은 뭐지? - User-Agent를 추가하면,서버에게 요청이 브라우저에서 온 것처럼 보이게 해서 차단 방지함

# 요청 및 HTML 파싱
response = requests.get(url, headers = headers) # headers를 왜 쓰는거지?
soup = BeautifulSoup(response.text, "html.parser")

# 상품 정보 추출
products = []
for item in soup.select(".s-result-item"):
    title = item.select_one("h2 .a-link-normal")
    price = item.select_one(".a-price-whole")
    if title and price:
        products.append({
            "상품명": title.text.strip(),
            "가격": price.text.strip()
        })

# 결과 출력
for product in products:
    print(f"상품명: {product['상품명']}, 가격: ${product['가격']}")