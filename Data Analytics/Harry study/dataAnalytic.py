# 1. 필요한 라이브러리 가져오기
import pandas as pd # pandas : 데이터 분석과 처리를 위한 라이브러리. 데이터를 테이블 형태로 다룬다.
import matplotlib.pyplot as plt # 데이터를 시각화 하는데 사용되는 라이브러리
from matplotlib import font_manager, rc # 한글 폰트 설정


# 1. 한글 폰트 경로 설정 (Windows 예시)
font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows에서는 '맑은 고딕' 사용
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 2. 데이터를 직접 코드에 입력하기
data = {
    "날짜": ["2024-11-10", "2024-11-10", "2024-11-10", "2024-11-11", "2024-11-11", "2024-11-11"],
    "음료 종류": ["아메리카노", "라떼", "녹차", "아메리카노", "라떼", "녹차"],
    "판매량": [30, 20, 15, 25, 18, 10],
    "가격 (NZD)": [4.5, 5.0, 4.0, 4.5, 5.0, 4.0],
}

# DataFrame으로 변환
df = pd.DataFrame(data)

# 3. 데이터 확인하기
print("데이터프레임 출력:")
print(df)

# 4. 총 판매량 계산
print("\n음료별 총 판매량:")
print(df.groupby("음료 종류")["판매량"].sum())

# 5. 날짜별 총 수익 계산
df["수익"] = df["판매량"] * df["가격 (NZD)"]
print("\n날짜별 총 수익:")
print(df.groupby("날짜")["수익"].sum())

# 6. 데이터 시각화
# 음료별 판매량 시각화
df.groupby("음료 종류")["판매량"].sum().plot(kind="bar", title="음료별 판매량")
plt.xlabel("음료 종류")
plt.ylabel("판매량")
plt.show()
