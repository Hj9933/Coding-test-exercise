import sys
input = sys.stdin.readline
n = int(input())
graph = [list(input()) for _ in range(n)]

# 가장 긴 연속된 사탕 수 확인 함수
def check():
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if graph[i][j] == graph[i][j-1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, n):
            if graph[j][i] == graph[j-1][i]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
    return max_cnt

answer = 0
for i in range(n):
    for j in range(n):
        # 오른쪽과 바꾸기
        if j + 1 < n:
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            answer = max(answer, check())
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
        # 아래와 바꾸기
        if i + 1 < n:
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
            answer = max(answer, check())
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]

print(answer)
