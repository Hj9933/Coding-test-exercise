n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

rank = [0]*n
for i in range(n):
    weight = lst[i][0]
    height = lst[i][1]
    for j in range(n):
        if lst[j][0] > weight and lst[j][1] > height:
            rank[i] += 1
for i in rank:
    print(i+1, end=' ')