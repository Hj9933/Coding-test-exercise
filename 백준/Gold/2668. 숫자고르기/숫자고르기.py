import sys
sys.setrecursionlimit(10**6)
# 2668. 숫자고르기
n = int(input())
lst = [[i] for i in range(n+1)]

for i in range(1,n+1):
    j = int(input())
    lst[i].append(j)

def dfs(x, start):
    visited[x] = True
    if not visited[lst[x][1]]:
        dfs(lst[x][1], start)
    elif visited[lst[x][1]] and lst[x][1]==start:
        ans.append(lst[x][1])
ans = []
for i in range(1, n+1):
    visited = [False]*(n+1)
    dfs(i, i)

print(len(ans))
ans.sort()
for i in ans:
    print(i)