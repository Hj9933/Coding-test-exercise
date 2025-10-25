# 2477. 참외밭 - 구현
n = int(input())

lengs = []

# 바깥면을 찾으려면 가장 긴 가로, 세로 길이를 먼저 찾아야 함

v_max, h_max = 0,0

for i in range(6):
    d, leng = map(int, input().split())
    if d == 1 or d==2:
        if h_max < leng:
            h_max = leng
            hmax_id = i
    else:
        if v_max < leng:
            v_max = leng
            vmax_id = i
    lengs.append(leng)

# 안쪽면은 가장 긴 변 양 옆 두 변의 차
h_inn = abs(lengs[(vmax_id-1)%6]-lengs[(vmax_id+1)%6])
v_inn = abs(lengs[(hmax_id-1)%6]-lengs[(hmax_id+1)%6])
result = (v_max*h_max-h_inn*v_inn)*n
print(result)