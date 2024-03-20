from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(start, end, visited):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        if now == end:
            print(visited[now]) # pop한 노드가 end 노드이면 프린트하고 반복문 종료
            break
        for i in (now-1, now+1, 2*now):
            if 0 <= i <= 100000 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[now] + 1 # 현재 노드에 +1


visited = [0]*(100001)

bfs(n, k, visited)
