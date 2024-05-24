from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        print(0)
    else:
        n = len(words) 
        len_word = len(target)
        graph = [[] for _ in range(n+1)]
        temp = []
        temp.append(begin)
        for i in range(n):
            if words[i] == target:
                target_id = i + 1
            temp.append(words[i]) 
        
        for i in range(n+1):
            a = temp[i]
            for j in range(n+1):
                if i != j:
                    b = temp[j]
                    cnt = 0
                    for k in range(len_word):
                        if a[k] == b[k]:
                            cnt += 1
                    if cnt == len_word - 1:
                        graph[i].append(j)
        def bfs(start, graph, visited):
            q = deque()
            q.append(start)
            visited[start] = 1
            flag = False
            while q:
                a = q.popleft()
                for i in graph[a]:
                    if i == target_id:
                        visited[i] = visited[a] + 1
                        return visited[i] - 1
                    if visited[i] == 0:
                        visited[i] = visited[a] + 1
                        q.append(i)
            return 0

        visited = [0]*(n+1)
        answer = bfs(0, graph, visited)
                        
            
    return answer