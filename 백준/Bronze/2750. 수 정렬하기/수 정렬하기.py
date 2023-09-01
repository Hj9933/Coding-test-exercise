import sys
input = sys.stdin.readline

n = int(input())
lst = list(int(input()) for _ in range(n))
lst.sort()
for i in range(n):
    print(lst[i])