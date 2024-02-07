import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(int(input()) for _ in range(n))

result = 0
for i in reversed(lst):
    if k // i != 0:
        result += k//i
        k = k%i
        if k == 0:
            break
print(result)