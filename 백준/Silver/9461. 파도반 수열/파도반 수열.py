t = int(input())
n = list(int(input()) for _ in range(t))
max_n = max(n)

dp = [1,1,1,2,2]
for i in range(5, max_n):
    dp.append(dp[i-5] + dp[i-1])

for n in n:
    print(dp[n-1])