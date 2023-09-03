import sys
input = sys.stdin.readline
lst = [list(input().split()) for _ in range(20)]

score = 0
total = 0
for i in range(20):
    if lst[i][2] == 'A+':
        score += float(lst[i][1]) * 4.5
        total += float(lst[i][1])
    elif lst[i][2] == 'A0':
        score += float(lst[i][1]) * 4.0
        total += float(lst[i][1])
    elif lst[i][2] == 'B+':
        score += float(lst[i][1]) * 3.5
        total += float(lst[i][1])
    elif lst[i][2] == 'B0':
        score += float(lst[i][1]) * 3.0
        total += float(lst[i][1])
    elif lst[i][2] == 'C+':
        score += float(lst[i][1]) * 2.5
        total += float(lst[i][1])
    elif lst[i][2] == 'C0':
        score += float(lst[i][1]) * 2.0
        total += float(lst[i][1])
    elif lst[i][2] == 'D+':
        score += float(lst[i][1]) * 1.5
        total += float(lst[i][1])
    elif lst[i][2] == 'D0':
        score += float(lst[i][1]) * 1.0
        total += float(lst[i][1])
    elif lst[i][2] == 'F':
        score += 0
        total += float(lst[i][1])

print(score/total)