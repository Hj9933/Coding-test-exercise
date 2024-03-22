import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort(key = lambda x: x[0])
    count = 1
    a = lst[0][1]
    for i in range(1, n):
        if lst[i][1] < a:
            count += 1
            a = lst[i][1]
    print(count)
    