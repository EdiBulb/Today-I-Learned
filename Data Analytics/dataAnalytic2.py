import pandas as pd

# 데이터 생성
data = {
    "이름" : ["김철수", "이영희", "박민수", "김철수", "이영희", "박민수"],
    "과목" : ["수학", "영어", "수학", "영어", "수학", "영어"], 
    "점수" : [85, 92, 78, 88, 90, 76],
}

# 데이터 프레임 생성
df = pd.DataFrame(data)

# 데이터 확인
print("데이터 프레임:\n", df)

# 과목별 평균 점수
print("\n과목별 평균 점수:")
print(df.groupby("과목")["점수"].mean())

# 학생별 총점
print("\n학생별 총점:")
print(df.groupby("이름")["점수"].sum())

# 과목별 최고 점수를 받은 학생
print("\n과목별 최고 점수를 받은 학생:")
idx = df.groupby("과목")["점수"].idxmax()
print(df.loc[idx, ["과목", "이름", "점수"]])
