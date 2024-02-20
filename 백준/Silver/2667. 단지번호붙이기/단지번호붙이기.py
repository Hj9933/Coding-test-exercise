n = int(input())
graph = [list(map(int, input())) for _ in range(n)]


# DFS 정의
def dfs(x,y):
    global count
    # 위치가 경로 밖으로 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 해당 위치를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 방문처리하고 해당 위치의 상,하,좌,우 위치도 재귀적 함수 호출
        graph[x][y] = 0
        count += 1 # 집 개수 + 1
        dfs(x-1, y) # 상
        dfs(x, y-1) # 좌
        dfs(x+1, y) # 하
        dfs(x, y+1) # 우
        return True
    return False

result = 0
count_1 = []
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j) == True:
            result += 1
            count_1.append(count)

print(result)
for i in sorted(count_1):
    print(i)