import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
cum_sum = [0]
total = 0
for i in range(n):
    total += num[i]
    cum_sum.append(total)

for _ in range(m):
    a, b = map(int, input().split())
    print(cum_sum[b] - cum_sum[a-1])