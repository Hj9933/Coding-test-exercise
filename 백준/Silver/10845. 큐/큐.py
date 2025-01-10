# 10845. 큐
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque([])
q_size = 0
for _ in range(n):
    cmd = list(input().split())
    if cmd[0] == 'push':
        q.append(cmd[1])
        q_size += 1
    elif cmd[0] == 'pop':
        if q:
            print(q.popleft())
            q_size -= 1
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(q_size)
    elif cmd[0] == 'empty':
        if q_size != 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if q_size != 0:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if q_size != 0:
            print(q[-1])
        else:
            print(-1)