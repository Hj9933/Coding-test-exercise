import sys

input = sys.stdin.readline

n = int(input())
step = [0]*301
for i in range(1, n+1):
    step[i] = int(input())
    
# ex. 10, 20, 15, 25, 10, 20
# 마지막에서부터 시작
# 두 가지 경우
# 1. n-1번째 계단으로 오는 경우: d[n] = d[n-3] + step[n-1] + step[n]
# 2. n-2번째 계단으로 오는 경우: d[n] = d[n-2] + step[n]
d = [0]*301 # 점수 합을 저장하는 DB 테이블
d[1] = step[1]
d[2] = step[1] + step[2]
d[3] = max(step[1] + step[3], step[2] + step[3])
for i in range(4, n+1):
    d[i] = max(d[i-3]+step[i-1]+step[i], d[i-2]+step[i])
print(d[n])