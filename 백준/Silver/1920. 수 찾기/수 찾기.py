n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

for i in range(m):
    l = 0
    u = n - 1
    idx = 0
    while l <= u:
        mid = (l + u) // 2
        if a[mid] == b[i]:
            idx = 1
            break
        elif a[mid] < b[i]:
            l = mid + 1
        else:
            u = mid - 1
    print(idx)