import sys
input = sys.stdin.readline

n = int(input())
queuestack = list(map(int, input().split()))
item = list(map(int, input().split()))
m = int(input())
input = list(map(int, input().split()))

# 스택 자료형은 무시, 큐만 하나의 큐처럼 생각; 스택이면 어차피 새로운 값 넣어도 그대로 새로운 값이 출력

from collections import deque

queue = deque([])
for i in range(n):
    if queuestack[i] == 0:
        queue.appendleft(item[i])
for i in range(m):
    queue.append(input[i])
    print(queue.popleft(), end = ' ')
