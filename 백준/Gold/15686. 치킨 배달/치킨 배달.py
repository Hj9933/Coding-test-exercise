import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))

# 치킨집 위치
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i,j))
INF = int(1e9)
# 치킨집 m개 뽑아서 최소 치킨 거리 구하기
from itertools import combinations
result = INF
for comb in combinations(chicken, m):
    min_dist = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                dist = INF
                for c in comb:
                    dist = min(abs(i-c[0])+abs(j-c[1]), dist)
                min_dist += dist
    result = min(result, min_dist)
print(result)