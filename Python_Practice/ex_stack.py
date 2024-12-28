stack = []

# 삽입
stack.append(10)
stack.append(20)
stack.append(30)

# 삭제
print(stack.pop())
print(stack.pop())
print(stack)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))

# Implementing a custom stack class
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushes:", stack.items)
print("Popped:", stack.pop())
print("Top element:", stack.peek())


def is_balanced(expression):
    stack = []
    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if not ((top == '(' and char == ')') or
                    (top == '{' and char == '}') or
                    (top == '[' and char == ']')):
                return False
    return len(stack) == 0

# Test
print(is_balanced("(())"))  # Output: True
print(is_balanced("([)]"))  # Output: False
