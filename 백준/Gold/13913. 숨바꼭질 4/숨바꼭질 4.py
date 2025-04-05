# 숨바꼭질 4
n, k = map(int, input().split())

INF = int(1e9)
visited = [INF]*200001
prev = [-1]*200001 # 경로 추적용
from collections import deque
def bfs(start):
    q = deque([])
    q.append(start)
    visited[start] = 0
    while q:
        now = q.popleft()
        if now == k:
            return 
        for next in (now-1, now+1,2*now):
            if 0 <= next <= 200000 and visited[next] == INF:
                visited[next] = visited[now] + 1
                prev[next] = now
                q.append(next)

bfs(n)
path = []
cur = k
while cur != -1:
    path.append(cur)
    cur = prev[cur]
path.reverse()
print(visited[k])
print(*path)