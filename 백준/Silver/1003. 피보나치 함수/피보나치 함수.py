# 0 -> 1 0
# 1 -> 0 1
# 2 -> 1 1
# 3 -> 1 2
# 4 -> 2 3
# 5 -> 3 5
# 6 -> 5 8

t = int(input())
dp = [[0] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]
dp[2] = [1,1]

for i in range(3, 41):
    dp[i] = [dp[i-1][1],dp[i-1][0]+dp[i-1][1]]

for _ in range(t):
    n = int(input())
    print(*dp[n])
