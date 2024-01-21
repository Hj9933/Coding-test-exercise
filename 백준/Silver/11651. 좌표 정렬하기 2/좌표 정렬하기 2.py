import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

lst_rev = []
for i in range(n):
    lst_rev.append([lst[i][1], lst[i][0]])
    
lst_rev.sort()
lst_rev1 = []
for i in range(n):
    lst_rev1.append([lst_rev[i][1], lst_rev[i][0]])

for i in range(n):
    print(*lst_rev1[i])