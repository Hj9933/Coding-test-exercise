from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    queue = deque()
    queue.append([numbers[0], 0]) # idx가 n이 될때 종료해야하므로 idx도 같이 기록
    queue.append([-1*numbers[0], 0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
        
    return answer