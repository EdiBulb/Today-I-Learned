for i in range(3):
    for j in range(4):
        print(f"i: {i}, j: {j}")
        

for i in range(1, 6):
    for j in range(i):
        print("*", end = "")
    print()

matrix = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end = " ")
    print()
    

# 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print()


# 사각형
for i in range(5):
    for j in range(5):
        print("*", end = " ")
    print()
    
# 좌표 출력
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end = " ")
    print()
    
# 홀수 좌표만 출력
for i in range(3):
    for j in range(3):
        if(i+j) % 2 ==1:
            print(f"({i}, {j})", end = " ")
    print()