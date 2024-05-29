import sys
input = sys.stdin.readline
import math
x, y = map(int, input().split())
z = int(y*100/x)

if x == y or z == 99:
    print(-1)
else:
    print(math.ceil(round((((z+1)*x/100)-y)*(100/(99-z)),4)))