import turtle

# 터틀 객체 생성
my_turtle = turtle.Turtle()

# 대시 선 그리기 함수
def draw_dash_line(length, dash_length, gap_length):
    for _ in range(int(length / (dash_length + gap_length))):
        my_turtle.forward(dash_length)  # 대시 부분
        my_turtle.penup()  # 펜 들어올리기
        my_turtle.forward(gap_length)  # 간격 부분
        my_turtle.pendown()  # 펜 내리기

# 대시 선 그리기
my_turtle.speed(1)  # 속도 설정
draw_dash_line(300, 20, 10)  # 전체 길이 300, 대시 길이 20, 간격 10

# 대기
turtle.done()
