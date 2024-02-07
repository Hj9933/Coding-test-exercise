import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst.sort() # 수 오름차순 정렬
count = 0
for i in range(n):
    count += sum(lst[0:i+1]) # i번째까지 더한 것을 count에 더해주기
print(count)