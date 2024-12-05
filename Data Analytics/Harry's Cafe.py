# 일주일 동아느이 메뉴별 판매 데이터 분석하기

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. 데이터 생성
np.random.seed(42)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
menu = ['Coffee', 'Tea', 'Sandwich', 'Cake']

# 매출 데이터 생성
data = {
    'Day': np.random.choice(days, size=50),
    'Menu Item': np.random.choice(menu, size=50),
    'Quantity': np.random.randint(1, 10, size=50),
    'Price': np.random.uniform(3.0, 10.0, size=50).round(2)
}

# DataFrame 생성
df = pd.DataFrame(data)
# 매출(Money Earned) 계산
df['Revenue'] = (df['Quantity']*df['Price']).round(2)

print("=== Harry's Cafe Data ===")
print(df.head()) # 데이터 확인

#2. 기본 통계 분석
print("\n===기본 통계 분석===")
print(df.describe()) # 데이터 통계 요약

# 메뉴별 총 매출
menu_revenue = df.groupby('Menu Item')['Revenue'].sum()
print("\n=== 메뉴별 총 매출===")
print(menu_revenue)


# 3. 요일별 매출 분석
day_revenue = df.groupby('Day')['Revenue'].sum()
print("\n===요일별 총 매출 ===")
print(day_revenue)

#4. 데이터 시각화
#메뉴별 매출 시각화
menu_revenue.plot(kind='bar', title = 'Menu Item Revenue', color = 'skyblue', ylabel='Revenue($)', xlabel="Menu Item", figsize=(8, 5))
plt.show()

# 요일별 매출 시각화
day_revenue.plot(kind='line', marker='o', title='Daily Revenue', ylabel='Revenue ($)', xlabel='Day', figsize=(8, 5))
plt.show()

# 5. 최고 매출 요일 및 메뉴 찾기
max_day = day_revenue.idxmax()
max_menu = menu_revenue.idxmax()
print(f"\nHarry's Cafe에서 가장 매출이 높은 요일은 {max_day}입니다.")
print(f"Harry's Cafe에서 가장 매출이 높은 메뉴는 {max_menu}입니다.")