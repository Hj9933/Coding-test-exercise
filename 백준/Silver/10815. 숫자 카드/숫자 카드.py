import sys
n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))

numbers = set(numbers)

result = []
for i in range(m):
    if lst[i] in numbers:
        result.append(1)
    else:
        result.append(0)
print(*result)