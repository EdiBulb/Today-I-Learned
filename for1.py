# 리스트 반복 repetation in list
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

# 숫자 범위 반복 repeat number range
for i in range(1, 6):
    print(i)


# 리스트에서 짝수 찾기
numbers = [10, 15, 20, 25, 30, 35, 40]

for number in numbers:
    if number%2 == 0:
        print(f"{number} is even")

# 문자열 순회
word = "Python"
for letter in word:
    print(letter)

# 리스트 안에 리스트 순회(중첩 for문)
matrix = [[1,2,3], [4,5,6], [7,9,0]]

for row in matrix:
    for num in row:
        print(num, end = " ")
    print()

# 리스트의 값 수정하기
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] +=2
print(numbers)

# 딕셔너리 순회
person = {'name': 'John', 'age':30, 'city':'New York'}

for key, value in person.items():
    print(f"{key}: {value}")


# 반복문 내에서의 조건문 연습
for i in range(1, 11):
    if i%2 == 0:
        print(f"{i} is even")
        