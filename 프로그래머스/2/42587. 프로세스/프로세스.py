from collections import deque
def solution(priorities, location):
    n = len(priorities)
    q = deque([])
    for i in range(n):
        q.append((priorities[i], i))

    answer = 0
    while q:
        a, loc = q.popleft()
        
        flag = False
        if any(a<item[0] for item in q):
            q.append((a, loc))
        else:
            answer += 1
            if loc == location:
                return answer
    return answer