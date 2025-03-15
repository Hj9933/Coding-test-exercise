# 1719. 빗물
h, w = map(int, input().split())
heights = list(map(int, input().split()))

rain = 0
max_tmp = heights[0]

for i in range(1,w-1):
    left_max = max(heights[:i])
    right_max = max(heights[i+1:])
    compare = min(left_max, right_max)
    if heights[i] < compare:
        rain += compare - heights[i]

print(rain)