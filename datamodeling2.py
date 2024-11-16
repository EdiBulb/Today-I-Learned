# 필요한 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt # 데이터 시각화
import seaborn as sns # 고급 시각화
from sklearn.model_selection import train_test_split # 훈련용과 테스트용 나눔
from sklearn.linear_model import LinearRegression # 선형 회귀 모델
from sklearn.metrics import mean_squared_error # 모델의 예측값과 실제 값 간의 차이를 평가
from matplotlib import font_manager, rc # 한글 폰트 설정


#  한글 폰트 경로 설정 (Windows 예시)
font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows에서는 '맑은 고딕' 사용
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 데이터 불러오기
df = pd.read_csv("fruit_sales.csv")


# 3. 데이터 탐색(Exploratory Data Analysis, EDA)
print("데이터 샘플:\n", df.head()) # 데이터프레임에서 첫 5개 행을 반환한다.
print("\n데이터 정보:")
print(df.info()) # 데이터프레임의 전체적인 정보를 출력한다.
print("\n결측값 확인:") 
print(df.isnull().sum()) # 결측값이 있는지 확인하기

# 데이터 시각화
# 과일별 판매량 비교
plt.figure(figsize=(7,6)) # 그래프 크기 설정
sns.barplot(x="과일", y="판매량", data=df, errorbar=None)
plt.title("과일별 판매량 비교")
plt.xlabel("과일")
plt.ylabel("판매량")
plt.show()

# 날짜별 판매량 추세
plt.figure(figsize=(8, 6))
sns.lineplot(x = "날짜", y = "판매량", hue = "과일", data = df)
plt.title("날짜별 판매량 추세")
plt.xlabel("날짜")
plt.ylabel("판매량")
plt.xticks(rotation = 45)
plt.show()

# 데이터 준비
# 입력 변수와 출력 변수 설정
X = df[["가격(개당)"]]
y = df["판매량"]

# 훈련 데이터와 테스트 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 에측
y_pred = model.predict(X_test)

# 성능 평가
mse = mean_squared_error(y_test, y_pred)
print("\n모델 성능 (MSE):", mse)

## 9. 예측 결과 시각화
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.title("실제 값과 예측 값 비교")
plt.xlabel("실제 값")
plt.ylabel("예측 값")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')  # 기준선
plt.show()