# 18115. 카드놓기
from collections import deque
n = int(input())
cmd = list(reversed(list(map(int, input().split()))))

result = deque([])
for i in range(n):
    if cmd[i] == 1:
        result.appendleft(i+1)
    elif cmd[i] == 2:
        result.insert(1, i+1)
    elif cmd[i] == 3:
        result.append(i+1)

print(*result)