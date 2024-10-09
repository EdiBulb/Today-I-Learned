# 물건을 세는 데코레이터

def count_items_decorator(func):
    def wrapper(*args, **kwargs):
        print("Let me count your items...")
        result = func(*args, **kwargs)
        print(f"You have purchased {result} items in total!")
        return result
    return wrapper

@count_items_decorator
def purchase_items(items):
    return len(items)

# 손님이 고른 물건들
customer_items = ['item1', 'items2', 'item3']

purchase_items(customer_items)