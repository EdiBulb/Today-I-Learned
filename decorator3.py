def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if not user.has_permission:
            print("Access Denied")
            return
        return func(user, *args, **kwargs) # 원래 함수
    return wrapper


@requires_permission
def access_sensitive_data(user):
    print("Sensitive Data Accessed")

class User:
    def __init__(self, has_permission):
        self.has_permission = has_permission

user1 = User(has_permission=True) # 권한 있음
user2 = User(has_permission=False) # 권한 없음

access_sensitive_data(user1) # 권한 있는 사용자 1
access_sensitive_data(user2) # 권한 없는 사용자 2

