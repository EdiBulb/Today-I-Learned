'''Types of Data Structures'''
'''
1. Linear Data Structure
- Arrays/List
- Stacks
- Queues

2. Non - Linear Data Structures
- Trees
- Graphs

3. Hash-Based Data Structures
- Hash Tables

'''
# 1. Lists
fruits = ["apple", "banana", "cherry"]

print(fruits[0])
fruits.append("data")

fruits.remove("banana")

# Iterate through the list
for fruit in fruits:
    print(fruit)
    
# 2. Stacks
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())
print(stack.pop())

# 3. Queues
from collections import deque

queue = deque()

# Enqueue elements
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue elements
print(queue.popleft()) 
print(queue.popleft()) 

# 4. Dictionaries (Hash Tables)
person = {"name": "Alice", "age":25, "city":"New York"}

print(person["name"])

person["job"] = "Engineer"

del person["city"]

# Iterate through dictionary
for key, value in person.items():
    print(key, value)

# 5. Trees
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Create nodes
root = Node(10)
root.left = Node(5)
root.right = Node(15)

# Traverse tree(Inorder) - what is this??????????????????????????????
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end = " ")
        inorder_traversal(node.right)

inorder_traversal(root)

# 6. Graphs
graph = {
    1:[2, 3],
    2:[4],
    3:[],
    4:[1]
}

# BFS Traversal
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
bfs(graph, 1)

# 7. Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1 | set2) # 1, 2, 3, 4, 5

# Intersection
print(set1 & set2)

# difference
print(set1 - set2)
