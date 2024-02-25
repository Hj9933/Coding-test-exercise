import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = list([] for _ in range(n+1))
for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(graph, i, visited)
    return visited
visited = [0]*(n+1)
visit = dfs(graph, 1, visited)
for i in range(2, n+1):
    print(visit[i])