import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
p = list(map(int, input().split()))

price = 0 # price 변수 생성
i = 0
while i < n:
    d = 0
    if p[i] == min(p[i:n-1]): # i번째부터 끝까지 중 최저 가격이라면 남은 거리만큼 모두 주유하고 반복문 마침
        price += sum(dist[i:])*p[i]
        break
    elif p[i] > p[i+1]: # 최저 가격이 아니고 다음 도시의 주유비보다 현재 도시의 주유비가 비싸다면 가야하는 거리만큼만 주유
        price += dist[i]*p[i]
        i += 1
    else: # 최저 가격이 아니고 다음 도시의 주유비보다 현재 도시의 주유비가 더 싸거나 같다면 
        j = i # 현재 i를 j에 저장
        while p[i] <= p[j+1]: # 현재 가격이 그 이후 도시 가격보다 작을 동안 계속 반복
            d += dist[j] # 다음 도시의 거리를 d에 합
            j += 1 # 그 다음 도시 가격 보기 위해 j+1
        price += d*p[i] # d거리만큼 주유
        i = j # j번째 도시까지 주유 했으므로 i=j
print(price)