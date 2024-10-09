# 버스 교통비 페이하기

def hi_decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello, Good morning")
        result = func(*args, **kwargs)
        print(f"Here is {result}")
    return wrapper

@hi_decorator
def payment(number):
    price = number * 4.5 # bus fee is 4.5$ per person.
    return price

number = 3
payment(number)