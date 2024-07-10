import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = list([] for _ in range(n))
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(start, visited, cnt):
    global flag
    if cnt == 5:
        flag = True
        return 

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, visited, cnt+1)
            visited[i] = False


flag = False
for i in range(n):
    visited = [False]*n
    visited[i] = True
    dfs(i, visited, 1)
    if flag == True:
        print(1)
        break
if flag == False:
    print(0)
