n = int(input())

from collections import deque
que = deque(range(1, n+1))

while len(que) != 1:
    que.popleft()
    if len(que) <= 1:
        break
    else:
        que.rotate(-1)

print(que[0])