n, m, v = map(int, input().split())
graph = list([] for _ in range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 정의
def dfs(graph, v, visited):
    global lst
    visited[v] = True #  현재노드 방문처리
    lst.append(v)
    # 현재 노드와 연결된 다른 노드들 재귀적으로 방문
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)
    return lst
            
visited = [False]*(n+1)
lst = []
print(*dfs(graph, v, visited))

from collections import deque
# bfs 메서드 정의
def bfs(graph, start, visited):
    lst = []
    queue = deque([start])
    visited[start] = True # 현재 노드 방문처리
    # 큐가 빌때까지 반복
    while queue:
        v = queue.popleft()
        lst.append(v)
        # 해당 원소와 연결된 아직 방문하지 않은 노드 queue에 넣기
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i) 
                visited[i] = True
    return lst

visited = [False]*(n+1)
print(*bfs(graph,v, visited))