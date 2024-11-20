import pandas as pd

data = {
    "고객 ID" : [101, 102, 103, 104, 105, 106], 
    "나이" : [25, 30, 22, 45, 35, 28],
    "성별" : ["남성", "여성", "여성", "남성", "여성", "남성"],
    "구매 금액 (NZD)" : [120, 200, 50, 300, 400, 150],
    "카테고리" : ["전자제품", "가구", "의류", "전자제품", "가구", "의류"], 
    "구매 날짜" : ["2024-11-10","2024-11-10","2024-11-11","2024-11-11","2024-11-11","2024-11-12"],
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 데이터 확인
print("데이터 프레임:\n", df)

# 카테고리별 총 구매 금액 계산
print("\n카테고리별 총 구매 금액:")
print(df.groupby("카테고리")["구매 금액 (NZD)"].sum())

# 성별로 평균 구매 금액 계산
print("\n성별 평균 구매 금액:")
print(df.groupby("성별")["구매 금액 (NZD)"].mean())

# 구매 금액이 100 이상인 고객 필터링
filtered = df[df["구매 금액 (NZD)"] >= 100]
print("\n구매 금액이 100 이상인 고객:\n", filtered)
print("\n100 이상 구매 고객의 평균 나이:")
print(filtered["나이"].mean())

# 날짜별 최고 구매 금액 고객
print("\n날짜별 최고 구매 금액 고객:")
idx = df.groupby("구매 날짜")["구매 금액 (NZD)"].idxmax()
print(df.loc[idx, ["구매 날짜", "고객 ID", "구매 금액 (NZD)"]])

# 사용자 정의 함수로 나이 그룹 분류
def age_group(age):
    if age < 30:
        return "청년"
    elif age < 50:
        return "중년"
    else:
        return "노년"
    
df["나이 그룹"] = df["나이"].apply(age_group)
print("\n나이 그룹별 총 구매 금액:")
print(df.groupby("나이 그룹")["구매 금액 (NZD)"].sum())
