if __name__ == '__main__':
    n = int(input("number of studnets?:")) # number of students
    student_marks = {} # dictionary - name : scores
    
    for _ in range(n):
        name, *line = input("name and scores: ").split() # name - name, line - group of scores.
        scores = list(map(float, line)) # change data type to float
        student_marks[name] = scores # put scores in dictionary
    
    # query     
    query_name = input("who are you looking for?: ")
    # if the name is in dic.
    # if query_name in student_marks:
    #     for i in range(3):
    #         scores_sum += student_marks[query_name][i]
    #     average = scores_sum/3.0
    values = student_marks[query_name]
    average = sum(values) / len(values)
    
    print(f"{average:.2f}")

    # if not. 