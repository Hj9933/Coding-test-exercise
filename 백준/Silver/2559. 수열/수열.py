import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
temp = list(map(int, input().split()))

window = deque()
current_max = float('-inf')
current_sum = 0
for i, v in enumerate(temp):
    window.append(v)
    current_sum += v
    if i < k-1: 
        continue
    
    current_max = max(current_max, current_sum)
    current_sum -= window.popleft()
    

print(current_max)