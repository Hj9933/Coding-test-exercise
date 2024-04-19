from collections import deque
import sys
# input = sys.stdin.readline
char = deque(list(input()))
q = deque([])
q_1 = deque([])
while char:
    a = char.popleft()
    if a == '<':
        print(*q, sep='', end='')
        q = deque([])
        q_1.append(a)
        while a != '>':
            a = char.popleft()
            q_1.append(a)
        print(*q_1, sep='', end='')
        q_1 = deque([])
    elif a == ' ':
        print(*q, sep='', end=' ')
        q = deque([])
    else:
        q.appendleft(a)
print(*q, sep='', end='')