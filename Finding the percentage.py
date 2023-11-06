if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    
    l = student_marks.get(query_name)

    result =  sum(l)/3

    print(f'{result:.2f}')  