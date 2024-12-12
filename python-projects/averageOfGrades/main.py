n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

arr = student_marks.get(query_name)

def findAverage(arr):
    average = 0.00
    sum = 0
    for score in arr:
        sum = sum + float(score)
    
    average = sum / 3
    return format(average, ".2f")

print(findAverage(arr))
    