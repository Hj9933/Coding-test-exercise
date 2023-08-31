from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
lst = [list(input().split()) for _ in range(n)]

d = deque()
for i in range(n):
    if lst[i][0] == '1':
        d.appendleft(int(lst[i][1]))
    elif lst[i][0] == '2':
        d.append(int(lst[i][1]))
    elif lst[i][0] == '3':
        if len(d) > 0:
            print(d.popleft())
        else:
            print(-1)
    elif lst[i][0] == '4':
        if len(d) > 0:
            print(d.pop())
        else:
            print(-1)
    elif lst[i][0] == '5':
        print(len(d))
    elif lst[i][0] == '6':
        if len(d) > 0 :
            print(0)
        else:
            print(1)
    elif lst[i][0] == '7':
        if len(d) > 0:
            print(d[0])
        else:
            print(-1)
    elif lst[i][0] == '8':
        if len(d) > 0:
            print(d[-1])
        else:
            print(-1)
