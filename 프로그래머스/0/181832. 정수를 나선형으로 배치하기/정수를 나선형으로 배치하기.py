# Python 풀이 : Crush on Study
def solution(n):
    answer = [[0]*n for _ in range(n)]
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    sy,sx = 0,0
    answer[sy][sx] = 1

    d = 0 # 동쪽 바라봄
    for _ in range(n*n):
        ny = sy+dy[d]
        nx = sx+dx[d]
        if 0<=ny<n and 0<=nx<n:
            if answer[ny][nx] == 0:
                answer[ny][nx] = answer[sy][sx] + 1
                sy,sx = ny,nx

            elif answer[ny][nx] != 0:
                d = (d+1)%4
                ny = sy+dy[d]
                nx = sx+dx[d]
                if 0<=ny<n and 0<=nx<n:
                    if answer[ny][nx] == 0:
                        answer[ny][nx] = answer[sy][sx] + 1
                        sy,sx = ny,nx

        else:
            d = (d+1)%4
            ny = sy+dy[d]
            nx = sx+dx[d]
            if 0<=ny<n and 0<=nx<n and answer[ny][nx] == 0:
                answer[ny][nx] = answer[sy][sx] + 1
                sy,sx = ny,nx


    return answer