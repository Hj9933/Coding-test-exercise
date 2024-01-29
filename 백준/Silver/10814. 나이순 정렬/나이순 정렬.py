n = int(input())
lst = [list(input().split()) for _ in range(n)]

lst.sort(key=lambda x: int(x[0]))

for i in range(len(lst)):
    print(*lst[i])