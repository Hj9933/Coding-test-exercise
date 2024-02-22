import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = list([] for _ in range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 1
def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    graph[v].sort()
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)
            
    return visited

visited = [0]*(n+1)

print(*dfs(graph, r, visited)[1:])