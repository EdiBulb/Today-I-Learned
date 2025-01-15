# 1. 필요한 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 2. 데이터 불러오기
df = pd.read_csv("housing_data.csv")

# 3. 데이터 탐색
print("데이터 샘플:\n", df.head())
print("\n데이터 정보:")
print(df.info())
print("\n결측값 확인:")
print(df.isnull().sum())

# 4. 데이터 시각화 (탐색적 데이터 분석)
# 면적과 가격의 관계
plt.figure(figsize=(8, 6))
sns.scatterplot(x="면적(제곱미터)", y="가격(만원)", data=df)
plt.title("면적과 가격의 관계")
plt.xlabel("면적(제곱미터)")
plt.ylabel("가격(만원)")
plt.show()

# 방 개수와 가격의 관계
plt.figure(figsize=(8, 6))
sns.boxplot(x="방 개수", y="가격(만원)", data=df)
plt.title("방 개수와 가격의 관계")
plt.xlabel("방 개수")
plt.ylabel("가격(만원)")
plt.show()

# 5. 데이터 준비
# 입력 변수와 출력 변수 설정
X = df[["면적(제곱미터)", "방 개수", "건축 연도"]]
y = df["가격(만원)"]

# 훈련 데이터와 테스트 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 7. 예측
y_pred = model.predict(X_test)

# 8. 성능 평가
mse = mean_squared_error(y_test, y_pred)
print("\n모델 성능 (MSE):", mse)

# 9. 예측 결과 시각화
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.title("실제 값과 예측 값 비교")
plt.xlabel("실제 값")
plt.ylabel("예측 값")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')  # 기준선
plt.show()
