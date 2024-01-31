import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))

# 떡볶이 떡이랑 같음
# 0부터 나무 중 최대길이 내에서 이분탐색

start = 1
end = max(height)

while start <= end:
    mid = (start+end)//2
    total = 0
    for i in height:
        if i > mid:
            total += i - mid
    
    if total < m: # 절단된 나무 높이가 m보다 작으면 높이를 줄여야함(왼쪽탐색)
        end = mid - 1
    else: # 절단된 나무 높이가 m보다 크거나 같으면 높이를 키워가면서 최댓값 찾기
        start = mid + 1

print(end)