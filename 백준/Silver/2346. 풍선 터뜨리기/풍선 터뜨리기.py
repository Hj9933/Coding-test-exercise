from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
arr = deque(enumerate(map(int,input().split()),start = 1))

# 커서를 이동하는 개념으로 이해해야함
ans = []
idx = 0
while arr:
    if idx > 0: # idx가 0보다 크면 arr의 맨 앞을 빼서 맨 뒤로 붙이기(idx만큼 커서를 앞으로 이동)
        a,b = arr.popleft()
        arr.append((a,b))
        idx -=1
    elif idx < 0: # idx가 0보다 작으면 arr의 맨 뒤를 빼서 맨 앞으로 붙이기(idx만큼 커서를 뒤로 이동)
        a,b = arr.pop()
        arr.appendleft((a,b))
        idx +=1
    else: # idx가 0이 되었을 때 커서의 위치가 올바른 것이므로 커서 위치에 있는 원소를 빼서 ans에 넣어줌
        a,b = arr.popleft()
        ans.append(a)
        if b > 0:
            idx = b-1
        else:
            idx = b
print(*ans) # *은 리스트 타입의 ans을 unpackaging 하기 위해 사용