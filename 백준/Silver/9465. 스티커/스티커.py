import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    sticker = list(list(map(int, input().split())) for _ in range(2))
    dp = list([0]*(n+1) for _ in range(2))
    dp[0][1], dp[1][1] = sticker[0][0], sticker[1][0]

    for i in range(2, n+1):
        dp[0][i] = max(dp[1][i-1]+sticker[0][i-1], dp[1][i-2]+sticker[0][i-1])
        dp[1][i] = max(dp[0][i-1]+sticker[1][i-1], dp[0][i-2]+sticker[1][i-1])
    print(max(dp[0][n], dp[1][n]))