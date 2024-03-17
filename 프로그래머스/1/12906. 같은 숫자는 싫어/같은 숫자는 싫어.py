from collections import deque
def solution(arr):
    answer = []
    answer.append(arr[0])
    queue = deque()
    queue.append(arr[0])
    pop = 0
    for i in range(1,len(arr)):
        pop = queue.pop()
        if pop == arr[i]:
            queue.append(pop)
        else:
            queue.append(arr[i])
            answer.append(arr[i])
            
    return answer