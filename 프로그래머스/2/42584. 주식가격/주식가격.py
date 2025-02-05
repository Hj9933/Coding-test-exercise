from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        dur = 0
        x = q.popleft()
        for i in q:
            if x <= i:
                dur += 1
            else:
                dur += 1
                break
        answer.append(dur)
            
    return answer