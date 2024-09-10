# 퇴사
n = int(input())
tp = [[] for _ in range(21)]
for i in range(1, n+1):
    t, p = map(int, input().split())
    tp[i+t-1].append((t,p))

dp = [0]*16
for i in range(1, n+1):
    if len(tp[i]) > 0:
        temp = 0
        for lst in tp[i]:
            temp = max(temp, dp[i-lst[0]]+lst[1])
        dp[i] = max(temp, max(dp))
    else:
        dp[i] = max(dp)
print(dp[n])