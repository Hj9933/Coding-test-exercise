import math
a, b, c = map(int, input().split())
if c-b == 0 or a/(c-b) < 0:
    print(-1)
else:
    print(math.floor(a/(c-b))+1)