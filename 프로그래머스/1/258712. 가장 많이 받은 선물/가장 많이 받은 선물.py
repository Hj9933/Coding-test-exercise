def solution(friends, gifts):

    n = len(friends)
    dic = {}
    for i in range(n):
        dic[friends[i]] = i
    graph = [[0]*n for _ in range(n)]
    for i in gifts:
        a, b = i.split()
        graph[dic[a]][dic[b]] += 1
    num_next = [0]*n
    visited = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and visited[i][j] == 0:
                visited[i][j] = 1
                visited[j][i] = 1
                if graph[i][j] != 0 or graph[j][i] != 0:
                    if graph[i][j] > graph[j][i]:
                        num_next[i] += 1
                    elif graph[i][j] < graph[j][i]:
                        num_next[j] += 1
                if graph[i][j] == graph[j][i]:
                    a = sum(graph[i])-sum([k[i] for k in graph])
                    b = sum(graph[j])-sum([k[j] for k in graph])
                    if a > b:
                        num_next[i] += 1
                    elif a < b:
                        num_next[j] += 1
    answer = max(num_next)        
        
    return answer