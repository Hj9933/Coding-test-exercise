import sys
sys.setrecursionlimit(10**6)

def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            dfs(n, computers, i, visited)
            answer += 1
    return answer

def dfs(n, computers, v, visited):
    visited[v] == 1
    for connect in range(n):
        if connect != v and computers[v][connect] == 1:
            if visited[connect] == 0:
                visited[connect] = 1
                dfs(n, computers, connect, visited)

    
    
    