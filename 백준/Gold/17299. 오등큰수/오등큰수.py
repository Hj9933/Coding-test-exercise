# 오등큰수
from collections import deque
n = int(input())
A = list(map(int, input().split()))

F = {}
for i in A:
    if i not in F:
        F[i] = 1
    else:
        F[i] += 1
        
result = [-1]*n
stack = [0]
for i in range(1, n):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        result[stack.pop()] = A[i]
    stack.append(i)
print(*result)