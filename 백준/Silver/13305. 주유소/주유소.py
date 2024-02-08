import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
p = list(map(int, input().split()))

min_p = p[0]
price = p[0] * dist[0]

for i in range(1, n-1):
    if min_p < p[i]: # 현재 min 가격이 현재 위치의 가격보다 작으면 현재 min가격으로 주유
        price += min_p * dist[i]
    else: # 현재 min 가격이 현재 위치의 가격보다 크거나 같으면 현재 위치 가격을 min으로 설정하고 min가격으로 주유
        min_p = p[i]
        price += min_p * dist[i]
print(price)