import time

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with {args} {kwargs} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def process_data(data):
    print(f"Processing data: {data}")
    
# 함수 호출
process_data("User Data")