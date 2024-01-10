n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort()
for i in range(n):
    print(*lst[i])