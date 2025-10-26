# 11057. 오르막수
n = int(input())

dp = [[0]*10 for _ in range(n+1)]
dp[0] = [1]*10

for i in range(1,n+1):
    dp[i][0] = 1
    for j in range(1,10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(dp[n][9]%10007)