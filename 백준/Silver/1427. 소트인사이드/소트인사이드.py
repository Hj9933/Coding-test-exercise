import sys
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, str(n)))
for i in sorted(num_list, reverse=True):
    print(i, end='')