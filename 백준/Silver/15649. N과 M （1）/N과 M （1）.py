import sys
import itertools
input = sys.stdin.readline

a, b = map(int, input().split())
arr = list(i for i in range(1, a+1))

for perm in itertools.permutations(arr, b):
    print(*perm)