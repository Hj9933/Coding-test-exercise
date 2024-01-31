import sys 
input = sys.stdin.readline

k, n = map(int, input().split())
lst = list(int(input()) for _ in range(k))

# 랜선이 가질 수 있는 최대길이를 찾아낸 후 0부터 최대값 사이에서 이분탐색
# 만들 수 있는 랜선 개수를 타깃으로
start = 1 
end = sum(lst)//n # 가지고 있는 랜선길이의 합을 필요한 랜선 개수로 나눈 몫이 만들 수 있는 최대값

while start <= end:
    mid = (start + end)//2 
    count = 0
    for i in lst: # 만들 수 있는 랜선개수 카운트
        count += i//mid

    if count < n: # 카운트가 타깃 n보다 작으면 왼쪽 탐색(길이 줄이기)
        end = mid - 1
    else: # 카운트가 타깃 n보다 같거나 크면 오른쪽 탐색(조건 만족하기 시작하면 루프문이 돌수록 최대값을 찾아나감)
        start = mid + 1

print(end) 