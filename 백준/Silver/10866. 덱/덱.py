from collections import deque
n = int(input())
lst = [list(input().split()) for _ in range(n)]

deque = deque()
for i in lst:
    if i[0] == 'push_front':
        deque.appendleft(int(i[1]))
    elif i[0] == 'push_back':
        deque.append(int(i[1]))
    elif i[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            a = deque.popleft()
            print(a)
    elif i[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            a = deque.pop()
            print(a)
    elif i[0] == 'size':
        print(len(deque))
    elif i[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif i[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque)-1])