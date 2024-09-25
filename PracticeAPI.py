import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    print(f"응답 코드: {response.status_code}")  # 응답 코드 출력

    if response.status_code == 200:
        return response.json()  # JSON 형식으로 응답 반환
    else:
        print(f"오류 메시지: {response.text}")  # 오류 메시지 출력
        return None  # 오류 처리

# 사용 예시
api_key = "f1a9cbd27abe2b22fd966f3723a4145b"  # 실제 API 키로 교체
city = "Auckland, NZ"  # 도시 이름에 국가 코드 추가
weather_data = get_weather(city, api_key)

if weather_data:
    print(f"{city}의 현재 온도: {weather_data['main']['temp']}°C")
else:
    print("날씨 데이터를 가져오는 데 실패했습니다.")
