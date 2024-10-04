import pandas as pd

# TF- IDF 벡터화
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 데이터프레임 생성
data = {
    'title': ['Auckland', 'Wellington', 'Christchurch', 'Queenstown', 'Rotorua'], 
    'description': [
        'Beautiful harbor city with stunning beaches.',
        'Capital city with vibrant culture and arts.', 
        'Garden city known for its beautiful parks', 
        'Adventure capital with amazing outdoor activities.', 
        'Famous for its geothermal activity and Maori culture'
    ]
}

df = pd.DataFrame(data)


# TF-IDF 벡터화
tfidf = TfidfVectorizer(stop_words='english') # 불용어 제거 - english
tfidf_matrix = tfidf.fit_transform(df['description'])

# Cosine 유사도 계산
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


# 추천 함수
def get_recommendations(title):
    # 입력된 제목의 인덱스 찾기
    idx = df.index[df['title'] == title].tolist()[0]

    # 유사도 점수 계산
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도 점수 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse = True)

    # 가장 유사한 2개의 여행지 인덱스 가져오기
    sim_scores = sim_scores[1:3] # 상위 2개 추천
    movie_indices = [i[0] for i in sim_scores]

    return df['title'].iloc[movie_indices]


# print(df)

recommeded_places = get_recommendations('Queenstown')
print("추천 여행지: ", recommeded_places.tolist())

