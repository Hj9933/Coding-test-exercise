# 컴퓨터의 수
v = int(input())
# 네트워크 쌍 개수
e = int(input())
# 반드시 graph[a]와 graph[b]에 동시에 연결 정보를 저장해야 한다.
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    # 연결된 컴퓨터의 정보가 언제가 1부터 등장한다는 보장 x
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, visited):
    global count
    visited[x] = True
    count += 1
    for node in graph[x]:
        if not visited[node]:
            dfs(node, visited)
        else:
            continue
count = 0
visited = [False] * (v+1)
dfs(1, visited)
print(count - 1)
