if __name__ == '__main__':
    # make list
    list = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())

        list.append([name, score])
    # print(list)
    
    # 점수 중복 제거 및 정렬 - 이해 부족
    scores = sorted(set([student[1] for student in list]))
    print(scores)
    
    
    
    # 밑에서 두번째 작은 수 찾아야함 - 정렬하면 되는구나...
    second_lowest_score = scores[1]
    
    # 해당 점수를 가진 학생 이름 추출
    second_lowest_students = [student[0] for student in list if student[1] == second_lowest_score]
    
    # 두번째 작은 수 이름을 알파벳 순서로 정렬
    second_lowest_students.sort()
    
    # 출력
    for name in second_lowest_students:
        print(name)
        
    