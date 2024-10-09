# 버스 교통비 페이하기

def hi_decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello, Good morning")
        func(*args, **kwargs)
    return wrapper

@hi_decorator
def payment():
    print("BBIK")


payment()