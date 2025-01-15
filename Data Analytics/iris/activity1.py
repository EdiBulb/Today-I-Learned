

# 필요한 라이브러리
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 1. 데이터 로드
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target  # 레이블 추가 (0, 1, 2로 표시)

# 2. 데이터 정보 출력
print("=== Iris 데이터셋 ===")
print(df.head())  # 데이터 샘플 확인
print("\n=== 데이터 통계 ===")
print(df.describe())  # 기초 통계 정보

# 3. 각 클래스(target)의 분포 확인
print("\n=== 클래스 분포 ===")
print(df['target'].value_counts())

# 상관계수 계산
correlation_matrix = df.corr()
print("=== Iris 데이터 상관계수 ===")
print(correlation_matrix)

# Heatmap으로 상관계수 시각화
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
plt.title("Correlation Matrix for Iris Features")
plt.show()

# 4. 데이터 시각화
import matplotlib.pyplot as plt
import seaborn as sns

sns.pairplot(df, hue='target', diag_kind='kde', palette='bright')
plt.show()
