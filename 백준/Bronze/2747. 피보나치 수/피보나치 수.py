# 2747. 피보나치 수
n = int(input())
dp = []
dp.append(0)
dp.append(1)
for i in range(1,n):
    dp.append(dp[i-1] + dp[i])

print(dp[n])