import sys
input = sys.stdin.readline

# 메모리 초과 문제를 해결하기 위해 계수 정렬

n = int(input())
arr = [0] * (10000 + 1) # 입력값이 최대 10000개이므로 

for _ in range(n):
    arr[int(input())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)