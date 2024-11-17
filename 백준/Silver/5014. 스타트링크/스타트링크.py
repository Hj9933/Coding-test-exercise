# 5014. 스타트링크
from collections import deque
f, s, g, u, d = map(int, input().split())
graph = [[i+u, i-d] for i in range(f+1)]
def bfs(start):
    q = deque([])
    q.append(start)
    visited[start] = 0
    while q:
        nx = q.popleft()
        if nx == g:
            break
        for i in graph[nx]:
            if 0 < i <= f and visited[i] == False and i != s:
                visited[i] = visited[nx] + 1
                q.append(i)
    if not visited[g]:
        answer = "use the stairs"
    else:
        answer = visited[g]
    return answer

visited = [False]*(f+1)
if s == g:
    print(0)
else:
    print(bfs(s))