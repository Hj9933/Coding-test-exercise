from collections import deque
def solution(m, n, puddles):
    answer = 0
    dp = list([0]*(m+1) for _ in range(n+1))
    # dp에 각 좌표마다 최단경로로 올 수 있는 경우의 수를 저장
    # puddle인 경우, 갈 수 없는 경로로 -1 표시
    for puddle in puddles:
        dp[puddle[1]][puddle[0]] = -1  
    
    # 나머지는 왼쪽과 위칸의 경우의 수를 더한 값이 해당 경우의 수가 됨
    for i in range(1, n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                dp[i][j] = 1
            elif dp[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
            
    print(dp)
    answer = dp[n][m]%1000000007
    return answer