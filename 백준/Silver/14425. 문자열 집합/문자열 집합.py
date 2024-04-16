
n, m = map(int, input().split())
S = []
for _ in range(n):
    S.append(input())
lst = {}
for _ in range(m):
    M = input()
    if M in lst:
        lst[M] += 1
    else:
        lst[M] = 1
from collections import Counter
lst = Counter(lst)

count = 0
for char in S:
    count += lst[char]
print(count)