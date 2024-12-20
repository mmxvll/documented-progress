n = 5
arr = set(map(int, [57,57,-57,-57]))

highest = -1000
for score in arr:
    if highest < score:
        highest = score


runner_up = -1000
for score in arr:
    if score > runner_up and score != highest:
        runner_up = score

print(str(runner_up))
