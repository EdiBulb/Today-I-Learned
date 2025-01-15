import pandas as pd

# CSV 파일 읽기
df = pd.read_csv("student.csv")
print("데이터프레임:\n", df)

# CSV 파일 쓰기
# df.to_csv("output.csv", index = False)

print("\n과목별 평균 점수:")
print(df.groupby("과목")["점수"].mean())

# 학생별 총점 계산
print("\n학생별 총점:")
print(df.groupby("이름")["점수"].sum())

# 점수가 80 이상인 학생 필터림
print("\n점수가 80 이상인 데이터:")
print(df[df["점수"] >= 80])

# 결과를 새로운 CSV 파일로 저장하기
df[df["점수"]>=80].to_csv("high_scores.csv", index = False)
print("\n점수가 80 이상인 데이터가 high_scores.csv에 저장되었습니다.")