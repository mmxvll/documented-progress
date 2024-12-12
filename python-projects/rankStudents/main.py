students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

def printSecondLowest(arr):
        lowest = 1000
        secondLowest = 1000
        namesWithLowest = []

        for student in arr:
            if student[1] < lowest:
                secondLowest = lowest
                lowest = student[1]
            elif student[1] < secondLowest and student[1] != lowest:
                secondLowest = student[1]
        
        for student in arr:
            if student[1] == secondLowest:
                namesWithLowest.append(student[0])
        
        namesWithLowest = [n.capitalize() for n in namesWithLowest]        
        namesWithLowest.sort()
        
        for name in namesWithLowest:
            print(name)
            
printSecondLowest(students)
                