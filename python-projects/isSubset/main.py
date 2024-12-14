testCases = int(input())
caseResults = []
for _ in range(testCases):
    setALength = int(input())
    setA = set(input().split())
    setBLength = int(input())
    setB = set(input().split())
    caseResults.append(str(setA.issubset(setB)))

for case in caseResults:
    print(case)
