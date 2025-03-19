# 텀프로젝트
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
t = int(input())
def dfs(start):
    global ans
    visited[start] = True
    stack.append(start)
    if visited[nums[start]]:
        if nums[start] in stack:
            ans += len(stack[stack.index(nums[start]):])
        return True
    else:
        if dfs(nums[start]):
            return True
        
for _ in range(t):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [False]*(n+1)
    ans = 0
    
    for i in range(1, n+1):
        if not visited[i]:
            stack = []
            dfs(i)
    print(n - ans)