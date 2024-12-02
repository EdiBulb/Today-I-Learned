

# Nested Lists with Mixed Data
math_score = [
    ["Harry", 80], 
    ["Praew", 90],
    ["Sofie", 70],
    ["Sam", 80],
    ["Pree", 70]
]

# print name and score
for sublist in math_score:
    print(sublist, end = " ")

# print seperatlely
for sublist in math_score:
    for item in sublist:
        print(item, end = " ")
        
print(math_score[0])
print(math_score[0][0])
print(math_score[0][1])

# 평탄화 작업
# List comprehenshion with nested lists - 
flattened = [item for sublist in math_score for item in sublist]
print(flattened)

# adding or removing sub-list
math_score.append(["Sam", 50])
print(math_score)
math_score.pop(2)
print(math_score)

'''점수가 두번째로 작은 사람 뽑아내기'''
#1. 점수만 뽑아내고 중복 제거
scores = sorted(set([student[1] for student in math_score]))
# print(scores)

#2. 두번째 작은 수 추출
second_lowest_score = scores[1]

second_lowest_students = [student[0] for student in math_score if student[1] == second_lowest_score]

#두번째 작은 수 이름을 알파벳 순서로 정렬하기
second_lowest_students.sort()

#출력
for name in second_lowest_students:
    print(name)
    
    
'''두번쨰로 작은 키 맞추기'''

Info = [
    ["Harry", 177.6],
    ["Praew", 160],
    ["Chenyi", 162],
    ["Pree", 160],
    ["Hazel", 163]
]

heights = sorted(set([people[1] for people in Info]))

second_lowest_height = heights[1]

second_lowest_person = [people[0] for people in Info if(people[1] == second_lowest_height)]

second_lowest_person.sort()

for name in second_lowest_person:
    print(name)