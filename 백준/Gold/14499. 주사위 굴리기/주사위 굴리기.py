import sys
input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

# 주사위의 초기 상태: [윗면(1), 아래면(6), 앞면(5), 뒷면(2), 왼쪽면(4), 오른쪽면(3)]
dice = [0, 0, 0, 0, 0, 0]

# 이동 방향: 동(1), 서(2), 북(3), 남(4)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def roll_dice(direction):
    top, bottom, front, back, left, right = dice
    if direction == 1:  # 동 (오른쪽으로 회전)
        dice[0], dice[1], dice[4], dice[5] = left, right, bottom, top
    elif direction == 2:  # 서 (왼쪽으로 회전)
        dice[0], dice[1], dice[4], dice[5] = right, left, top, bottom
    elif direction == 3:  # 북 (위쪽으로 회전)
        dice[0], dice[1], dice[2], dice[3] = front, back, bottom, top
    elif direction == 4:  # 남 (아래쪽으로 회전)
        dice[0], dice[1], dice[2], dice[3] = back, front, top, bottom

for i in commands:
    nx, ny = x + dx[i - 1], y + dy[i - 1]

    # 지도 바깥으로 이동할 경우 명령 무시
    if not (0 <= nx < n and 0 <= ny < m):
        continue

    # 주사위 굴리기
    roll_dice(i)

    # 지도와 주사위 바닥면 간 값 처리
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[1]  # 주사위 바닥면의 값을 지도에 복사
    else:
        dice[1] = maps[nx][ny]  # 지도 값을 주사위 바닥면으로 복사
        maps[nx][ny] = 0

    # 주사위 윗면 출력
    print(dice[0])

    # 현재 위치 갱신
    x, y = nx, ny
