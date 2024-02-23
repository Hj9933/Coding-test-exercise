import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = list([] for _ in range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

def bfs(graph, start, visited):
    global cnt
    queue = deque([start])
    visited[start] = cnt
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        for i in sorted(graph[v], reverse=True):
            if visited[i] == 0:
                queue.append(i)
                cnt += 1
                visited[i] = cnt
    return visited
visited = [0]*(n+1)

cnt = 1
visit = bfs(graph, r, visited)
for i in range(1, n+1):
    print(visit[i])