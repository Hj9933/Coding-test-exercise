# 플루이드 워셜 알고리즘
# 사이클, 즉 다시 자기자신으로 돌아오는 최단거리를 구해야하므로 처음에 자기자신도 INF로 초기화해놓고 플루이드 워셜 알고리즘 수행. 이후 사이클 중 최소거리 출력
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
cycle = []
for i in range(1, v+1):
    cycle.append(graph[i][i])
cycle_min = min(cycle)
if cycle_min==INF:
    print(-1)
else:
    print(cycle_min)