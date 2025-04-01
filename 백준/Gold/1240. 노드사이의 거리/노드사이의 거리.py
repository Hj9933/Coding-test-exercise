import sys
input = sys.stdin.readline
# 노드 사이의 거리
n, m = map(int, input().split())
nodes = list([] for _ in range(n+1))

for _ in range(n-1):
    a, b, c = map(int, input().split())
    nodes[a].append((b,c))
    nodes[b].append((a,c))

def dfs(start, end):
    global dist
    if start == end:
        return True
    for i in nodes[start]:
        now, cost = i[0], i[1]
        if not visited[now]:
            visited[now] = True
            dist += cost
            if dfs(now, end):
                return True
            visited[now] = False
            dist -= cost

    


quest = list(list(map(int, input().split())) for _ in range(m))
for q in quest:
    visited = [False]*(n+1)
    dist = 0
    visited[q[0]] = True
    dfs(q[0], q[1])
    print(dist)
