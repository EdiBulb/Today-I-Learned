def my_decorator(func):
    def wrapper(): #wrapper 는 함수를 감싸는 역할을 한다. wrapper covers the other functions.
        print("Before the function is called")
        func()
        print("After the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")


say_hello()