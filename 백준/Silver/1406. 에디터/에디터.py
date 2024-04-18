from collections import deque
import sys
input = sys.stdin.readline
str_lst = list(input().strip('\n'))
n = int(input())

q = deque(str_lst) # 커서의 위치가 항상 맨 뒤에 위치하도록 큐를 두 개로 분리
q_1 = deque([])

for _ in range(n):
    command = list(input().strip('\n').split())
    if command[0] == 'L':
        if len(q) > 0:
            q_1.appendleft(q.pop()) # q의 맨 오른쪽 문자를 떼서 q_1 맨 왼쪽으로 붙이기
    if command[0] == 'D':
        if len(q_1) > 0:
            q.append(q_1.popleft()) # q_1의 맨 왼쪽 문자를 떼서 q 맨 오른쪽으로 붙이기
    if command[0] == 'B':
        if len(q) > 0:
            q.pop()
    if command[0] == 'P':
        q.append(command[1]) 
result = q + q_1
print(*result, sep='')