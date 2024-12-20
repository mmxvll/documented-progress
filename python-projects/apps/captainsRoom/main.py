membersPerGroup = int(input())
roomsList = list(input().split())

duplicates = set()
seen = set()

for num in roomsList:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

captainsRoom = []
for room in roomsList:
    if room not in duplicates:
        captainsRoom.append(room)

print(captainsRoom[0])
