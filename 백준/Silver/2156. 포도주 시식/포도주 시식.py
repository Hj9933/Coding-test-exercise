import sys
input = sys.stdin.readline
n = int(input())
drink = list(int(input()) for _ in range(n))
dp = list([0,0,0] for _ in range(n)) # 첫번째 마시는 경우, 두번째 마시는 경우, 안마시는 경우
dp[0][0] = drink[0]

for i in range(1, n):
    dp[i][0] = dp[i-1][2] + drink[i] # 처음 마시는 경우: 바로 전에 안마셨어야 함
    dp[i][1] = dp[i-1][0] + drink[i] # 두 번째 마시는 경우: 바로 전에 한번 마셨어야 함
    dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) # 안 마실 경우, 그 전에 한번 마신 경우와 두번 마신 경우 중 큰거

print(max(dp[n-1]))