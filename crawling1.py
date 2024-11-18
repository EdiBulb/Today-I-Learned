from selenium import webdriver
from selenium.webdriver.common.by import By

# 브라우저 실행
driver = webdriver.Chrome()  # ChromeDriver 설치 필요
driver.get("https://example.com")

# 데이터 추출
titles = driver.find_elements(By.CSS_SELECTOR, ".title")
for title in titles:
    print(title.text)

driver.quit()
