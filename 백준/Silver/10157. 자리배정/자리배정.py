c, r = map(int, input().split())
k = int(input())
seat = [[-1]*c for _ in range(r)]
dx = [-1,0,1,0] # 위, 오, 아래, 왼
dy = [0,1,0,-1]
d = 0
i = 2
x, y = r-1, 0 
seat[x][y] = 1
flag = False
if k == 1:
    print(1,1)
else:
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < r and 0 <= ny < c and seat[nx][ny] == -1:
            seat[nx][ny] = i
            x, y = nx, ny
            if i == k:
                print(y+1, r-x)
                flag = True
                break
        else:
            d += 1
            if d > 3:
                d = 0
            
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and seat[nx][ny] == -1:
                seat[nx][ny] = i
                x, y = nx, ny
                if i == k:
                    print(y+1, r-x)
                    flag = True
                    break
            else:
                break
        i += 1
    if not flag:
        print(0)