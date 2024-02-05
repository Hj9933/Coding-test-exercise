import sys
input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# f = a1*n+a0, g = c*n
# a1*n0+a0-c*n0 <= 0 -> 만족

if a1 > c:
    print(0)
elif a1 == c and a0 > 0:
    print(0)
elif a1 == c and a0 <= 0:
    print(1)
elif a1*n0 + a0 - c*n0 <= 0: # a1 < c 는 부등식 만족하면 1
    print(1)
else:
    print(0)


