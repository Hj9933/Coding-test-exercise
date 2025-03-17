# 키 순서
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
taller = list([] for _ in range(n+1))
smaller = list([] for _ in range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    taller[a].append(b)
    smaller[b].append(a)
taller_than = list([] for _ in range(n+1))
smaller_than = list([] for _ in range(n+1))
from collections import deque
def bfs(start, lst, lst1):
    q = deque([])
    visited[start] = True
    q.append(start)
    while q:
        now = q.pop()
        for i in lst[now]:
            if not visited[i]:
                lst1[start].append(i)
                visited[i] = True
                q.append(i)
for i in range(1, n+1):
    visited = [False]*(n+1)
    bfs(i, taller, taller_than)

for i in range(1,n+1):
    visited = [False]*(n+1)
    bfs(i, smaller, smaller_than) 

result = 0
for i in range(1,n+1):
    if len(smaller_than[i]) + len(taller_than[i]) == n-1:
        result += 1
print(result)