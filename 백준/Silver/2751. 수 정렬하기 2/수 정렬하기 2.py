import sys
input = sys.stdin.readline

n = int(input())
num = list(int(input()) for _ in range(n))

for i in sorted(num):
    print(i)