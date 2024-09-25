import turtle

def draw_stick_figure():
    # 머리
    turtle.penup()
    turtle.goto(0, 0)  # 시작 위치
    turtle.pendown()
    turtle.circle(20)  # 머리

    # 몸통
    turtle.penup()
    turtle.goto(0, 0)  # 머리 위치로 이동
    turtle.pendown()
    turtle.goto(0, -60)  # 몸통

    # 팔
    turtle.penup()
    turtle.goto(0, -20)  # 팔 위치
    turtle.pendown()
    turtle.goto(-30, -30)  # 왼쪽 팔
    turtle.penup()
    turtle.goto(0, -20)  # 팔 위치로 이동
    turtle.pendown()
    turtle.goto(30, -30)  # 오른쪽 팔

    # 다리
    turtle.penup()
    turtle.goto(0, -60)  # 다리 시작 위치
    turtle.pendown()
    turtle.goto(-30, -100)  # 왼쪽 다리
    turtle.penup()
    turtle.goto(0, -60)  # 다리 시작 위치로 이동
    turtle.pendown()
    turtle.goto(30, -100)  # 오른쪽 다리

def draw_girlfriend():
    # 머리
    turtle.penup()
    turtle.goto(100, 0)  # 시작 위치
    turtle.pendown()
    turtle.circle(20)  # 머리

    # 머리에 나비 핀 그리기 (오른쪽 위에)
    turtle.penup()
    turtle.goto(115, 20)  # 핀 위치
    turtle.pendown()
    turtle.goto(105, 30)  # 왼쪽 날개
    turtle.goto(115, 20)  # 핀 중앙으로 돌아오기
    turtle.goto(125, 30)  # 오른쪽 날개
    turtle.goto(115, 20)  # 핀 중앙으로 돌아오기

    # 몸통
    turtle.penup()
    turtle.goto(100, 0)  # 머리 위치로 이동
    turtle.pendown()
    turtle.goto(100, -60)  # 몸통

    # 팔
    turtle.penup()
    turtle.goto(100, -20)  # 팔 위치
    turtle.pendown()
    turtle.goto(70, -30)  # 왼쪽 팔
    turtle.penup()
    turtle.goto(100, -20)  # 팔 위치로 이동
    turtle.pendown()
    turtle.goto(130, -30)  # 오른쪽 팔

    # 다리
    turtle.penup()
    turtle.goto(100, -60)  # 다리 시작 위치
    turtle.pendown()
    turtle.goto(70, -100)  # 왼쪽 다리
    turtle.penup()
    turtle.goto(100, -60)  # 다리 시작 위치로 이동
    turtle.pendown()
    turtle.goto(130, -100)  # 오른쪽 다리

# 초기 설정
turtle.speed(1)  # 속도 설정
draw_stick_figure()  # 졸라맨 그리기
draw_girlfriend()  # 여자친구 그리기

turtle.hideturtle()  # 터틀 숨기기
turtle.done()  # 대기
